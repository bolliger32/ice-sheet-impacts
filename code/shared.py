from pathlib import Path

import geopandas as gpd
import xarray as xr
from distributed import Client
from distributed.diagnostics.plugin import UploadDirectory
from pyCIAM import __file__

DIR_SCRATCH = Path("/tmp/ciam-scratch")

SLIIDERS_VERS = "v1.2"
RES_VERS = "IS_v0.1"

# what are the GMSL values associated with the ice sheet contributions
IS_GMSL = 2.35

# Cloud Storage tools (will work with local storage as well but may need to be specifiec
# for cloud buckets
STORAGE_OPTIONS = {}


def _to_fuse(path):
    return Path(str(path).replace("gs://", "/gcs/"))


# Output dataset attrs
HISTORY = """version IS-v0.1: Version associated with Huprikar et al., 2024"""
AUTHOR = "Ian Bolliger"
CONTACT = "ian@reask.earth"


##################
# ROOT DIRECTORIES
##################
DIR_HOME = Path("../")
DIR_DATA = DIR_HOME / "data"
DIR_RAW = DIR_DATA / "raw"
DIR_INT = DIR_DATA / "int"
DIR_RES = DIR_HOME / f"results-{RES_VERS}"

##################
# MODEL PARAMS
##################

PATH_PARAMS = Path.home() / "git-repos/pyCIAM-public/params.json"

##################
# SOCIOECON INPUTS
##################

# SLIIDERS
PATH_SLIIDERS = DIR_RAW / f"sliiders-{SLIIDERS_VERS}.zarr"
PATH_SLIIDERS_SEG = DIR_INT / f"sliiders-{SLIIDERS_VERS}-seg.zarr"

#####
# SLR
#####

DIR_SLR_RAW = DIR_RAW / "slr"
DIR_SLR_INT = DIR_INT / "slr"

DIR_SLR_AR6_RAW = DIR_SLR_RAW / "ar6"
DIR_SLR_IS_RAW = DIR_SLR_RAW / "ice-sheet-contributions"
PATH_SLR_IS_RAW = DIR_SLR_IS_RAW / "ice-sheet-contributions.parquet"
PATH_SLR_INT = DIR_SLR_INT / "msl-rel-2005.zarr"


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


def upload_pyciam(client, restart_client=True):
    """Upload a local package to Dask Workers. After calling this function, the package
    contained at ``pkg_dir`` will be available on all workers in your Dask cluster,
    including those that are instantiated afterward. This package will take priority
    over any existing packages of the same name. This is a useful tool for working with
    remote dask clusters (e.g. via Dask Gateway) but is not needed for local clusters.
    If you wish to use this, you should call this function from within
    `start_dask_cluster`.

    Parameters
    ----------
    client : :py:class:`distributed.Client`
        The client object associated with your Dask cluster's scheduler.
    pkg_dir : str or Path-like
        Path to the package you wish to zip and upload
    **kwargs
        Passed directly to :py:class:`distributed.diagnostics.plugin.UploadDirectory`
    """
    client.register_worker_plugin(
        UploadDirectory(
            Path(__file__).parents[1],
            update_path=True,
            restart=restart_client,
            skip_words=(
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
            ),
        )
    )


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


def start_dask_cluster(**kwargs):
    client = Client(**kwargs)
    print(client.dashboard_link)
    return client
