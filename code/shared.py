import os
from pathlib import Path
from zipfile import ZipFile

import geopandas as gpd
import xarray as xr
from cloudpathlib import AnyPath
from dask_gateway import GatewayCluster
from pyCIAM import __file__
from typing import Dict

# DIR_SCRATCH = Path("/tmp/ciam-scratch")
DIR_SCRATCH = AnyPath("gs://rhg-data-scratch/ciam-scratch")

SLIIDERS_VERS = "v1.2"
RES_VERS = "IS_v0.2"

# what are the GMSL values associated with the ice sheet contributions
IS_GMSL = 2.35

# Cloud Storage tools (will work with local storage as well but may need to be specifiec
# for cloud buckets
STORAGE_OPTIONS: Dict[str, str] = {}


def _to_fuse(path):
    return Path(str(path).replace("gs://", "/gcs/"))


# Output dataset attrs
HISTORY = """version IS-v0.1: Version associated with Huprikar et al., 2024
version IS-v0.1.1: Bugfix on SLR in years 2005-2019
version IS-v0.2: Using 2% discount rate and updated 7.6 movefactor (instead of 8.8)"""
AUTHOR = "Ian Bolliger"
CONTACT = "ian@reask.earth"


##################
# ROOT DIRECTORIES
##################
# DIR_HOME = Path("../")
DIR_HOME = AnyPath("gs://rhg-data/impactlab-rhg/coastal/ice-sheet-impacts")
DIR_DATA = DIR_HOME / "data"
# DIR_RAW = DIR_DATA / "raw"
DIR_INT = DIR_DATA / "int"
DIR_RES = DIR_HOME / f"results-{RES_VERS}"

##################
# MODEL PARAMS
##################

PATH_PARAMS = Path.home() / "git-repos/ice-sheet-impacts/code/params.json"

##################
# SOCIOECON INPUTS
##################

# SLIIDERS

# PATH_SLIIDERS = DIR_RAW / f"sliiders-{SLIIDERS_VERS}.zarr"
PATH_SLIIDERS = AnyPath(
    "gs://rhg-data/impactlab-rhg/coastal/sliiders/output/sliiders-v1.2.zarr"
)

PATH_SLIIDERS_SEG = PATH_SLIIDERS.parent / (
    PATH_SLIIDERS.stem + "-seg" + PATH_SLIIDERS.suffix
)

#####
# SLR
#####
DIR_SLR = AnyPath("gs://rhg-data/impactlab-rhg/coastal/ciam_paper/data")
DIR_SLR_RAW = DIR_SLR / "raw" / "slr"
DIR_SLR_INT = DIR_INT / "slr"

DIR_SLR_AR6_RAW = DIR_SLR_RAW / "ar6"
# PATH_SLR_IS_RAW = DIR_SLR_RAW / "ice-sheet-contributions.parquet"
PATH_SLR_IS_RAW = AnyPath("../data/raw/slr/ice-sheet-contributions.parquet")
PATH_SLR_INT = DIR_SLR_INT / "msl-rel-2005-is.zarr"


###########################
# PYCIAM INTERMEDIATE FILES
###########################

PATHS_SURGE_LOOKUP = {}
for seg in ["seg_adm", "seg"]:
    PATHS_SURGE_LOOKUP[seg] = DIR_INT / f"surge-lookup-{SLIIDERS_VERS}-{seg}.zarr"

PATH_REFA = DIR_INT / f"refA_by_movefactor_{SLIIDERS_VERS}.zarr"

###########################
# PYCIAM OUTPUTS
###########################

PATH_OUTPUTS = DIR_RES / f"pyCIAM_{RES_VERS}_results.zarr"


# Make directories where needed
for p in [
    DIR_SCRATCH,
    DIR_RES,
]:
    p.mkdir(exist_ok=True, parents=True)


def _zipdir(
    path,
    zip_filename,
    skip_files=(
        ".git",
        ".github",
        ".pytest_cache",
        "tests",
        "docs",
        "deploy",
        "notebooks",
        ".ipynb_checkpoints",
        "__pycache__",
        ".coverage",
        "dockerignore",
        ".gitignore",
        ".gitlab-ci.yml",
        ".gitmodules",
        "pyclaw.log",
        "run_tests.sh",
    ),
):

    with ZipFile(zip_filename, "w") as ziph:
        for root, dirs, files in os.walk(path):
            for file in files:
                if any([f in file.split("/") for f in skip_files]):
                    continue
                # Create a relative path for files to preserve the directory structure
                # within the ZIP archive. This relative path is based on the directory
                # being zipped, so files are stored in the same structure.
                relative_path = os.path.relpath(
                    os.path.join(root, file), os.path.join(path, "..")
                )
                ziph.write(os.path.join(root, file), arcname=relative_path)


def upload_pyciam(client):
    package_dir = Path(__file__).parent
    zip_filename = "/tmp/pyCIAM.zip"  # Output ZIP file name
    _zipdir(package_dir, zip_filename)
    client.upload_file(zip_filename)


def save(obj, path, *args, **kwargs):
    if path.suffix == ".zarr":
        meth = "to_zarr"
    elif path.suffix == ".parquet":
        meth = "to_parquet"
    else:
        raise ValueError(type(obj))
    getattr(obj, meth)(str(path), *args, storage_options=STORAGE_OPTIONS, **kwargs)


def open_zarr(path, **kwargs):
    return xr.open_zarr(str(path), storage_options=STORAGE_OPTIONS, **kwargs)


def _generate_parent_fuse_dirs(path):
    return Path(path).parent.mkdir(exist_ok=True, parents=True)


def open_dataset(path, **kwargs):
    _path = str(_to_fuse(path))
    _generate_parent_fuse_dirs(_path)
    return xr.open_dataset(_path, **kwargs)


def open_dataarray(path, **kwargs):
    _path = str(_to_fuse(path))
    _generate_parent_fuse_dirs(_path)
    return xr.open_dataarray(_path, **kwargs)


def read_shapefile(path, **kwargs):
    _path = str(path).replace("gs://", "/gcs/")
    _generate_parent_fuse_dirs(_path)
    return gpd.read_file(_path, **kwargs)


def start_dask_cluster(profile="micro", **kwargs):
    img = os.environ["JUPYTER_IMAGE"]
    cluster = GatewayCluster(
        profile=profile, worker_image=img, scheduler_image=img, **kwargs
    )
    client = cluster.get_client()
    upload_pyciam(client)
    return client, cluster
