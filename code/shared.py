from distributed import Client
from pathlib import Path

DIR_SCRATCH = Path("/tmp")

SLIIDERS_VERS = "v1.2"
RES_VERS = "IS_v0.2"

# what are the GMSL values associated with the ice sheet contributions
IS_GMSL = 2.35

# Output dataset attrs
HISTORY = """version IS-v0.1: Version associated with Huprikar et al., 2024
version IS-v0.1.1: Bugfix on SLR in years 2005-2019
version IS-v0.2: Using 2% discount rate and updated 7.6 movefactor (instead of 8.8)"""
AUTHOR = "Ian Bolliger"
CONTACT = "ian@reask.earth"


##################
# ROOT DIRECTORIES
##################
DIR_HOME = Path("/")
DIR_DATA = DIR_HOME / "data"
DIR_RAW = DIR_DATA / "raw"
DIR_INT = DIR_DATA / "int"
DIR_RES = DIR_HOME / f"results"

##################
# MODEL PARAMS
##################

PATH_PARAMS = Path("params.json")

##################
# SOCIOECON INPUTS
##################

# SLIIDERS
PATH_SLIIDERS = DIR_RAW / f"sliiders-{SLIIDERS_VERS}.zarr"
PATH_SLIIDERS_SEG = PATH_SLIIDERS.parent / (
    PATH_SLIIDERS.stem + "-seg" + PATH_SLIIDERS.suffix
)

#####
# SLR
#####
DIR_SLR_RAW = DIR_RAW / "slr"
DIR_SLR_INT = DIR_INT / "slr"

DIR_SLR_AR6_RAW = DIR_SLR_RAW / "ar6"
PATH_SLR_IS_RAW = DIR_RAW / "ice-sheet-contributions.parquet"
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

def start_dask_cluster():
    # Code Ocean capsules run on 16-core machines by default.
    # This function can be changed to match your specs if running elsewhere
    client = Client(n_workers=16)
    cluster = client.cluster
    return client, cluster