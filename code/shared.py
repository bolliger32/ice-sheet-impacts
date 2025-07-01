"""Parameters and common functions to be used in notebook-based analysis workflow."""

from pathlib import Path

from distributed import Client

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
DIR_RES = DIR_HOME / "results"
DIR_FIGS = DIR_RES / "figures"

##################
# MODEL PARAMS
##################

PATH_PARAMS = Path("params.json")

##################
# SOCIOECON INPUTS
##################

# SLIIDERS
PATH_SLIIDERS = DIR_RAW / f"sliiders-{SLIIDERS_VERS}.zarr"
PATH_SLIIDERS_SEG = DIR_INT / f"sliiders-{SLIIDERS_VERS}-seg.zarr"
PATH_YPK_HIST = DIR_RAW / "ypk_2000_2020_20240222.parquet"
PATH_GRIDDED_GDP = DIR_RAW / "wang_and_sun_2020_gdp.tif"

#####
# SLR
#####
DIR_SLR_RAW = DIR_RAW / "slr"

DIR_SLR_AR6_RAW = DIR_SLR_RAW / "ar6"
PATH_SLR_IS_RAW = DIR_SLR_RAW / "ice-sheet-contributions.parquet"
PATH_SLR_INT = DIR_INT / "msl-rel-2005-is.zarr"
PATH_SLR_IS_GRID_ANT_RAW = DIR_SLR_RAW / "sea_ant86.txt"
PATH_SLR_IS_GRID_GR_RAW = DIR_SLR_RAW / "sea_green44.txt"

#########
# SPATIAL
#########

PATH_GADM = DIR_RAW / "gadm_410-levels.gpkg"
PATH_LANDSCAN = DIR_RAW / "landscan-global-2020.tif"

###########################
# PYCIAM INTERMEDIATE FILES
###########################

PATHS_SURGE_LOOKUP = {}
for seg in ["seg_adm", "seg"]:
    PATHS_SURGE_LOOKUP[seg] = DIR_INT / f"surge-lookup-{SLIIDERS_VERS}-{seg}.zarr"

PATT_REFA = DIR_INT / f"refA_by_movefactor_{SLIIDERS_VERS}_dr_{{dr}}.zarr"

#########
# OUTPUTS
#########

PATT_OUTPUTS = DIR_INT / f"pyCIAM_{RES_VERS}_results_dr_{{dr}}.zarr"
PATHS_MAPS = {
    kind: str(DIR_FIGS / "{dr}" / f"SCISM-maps-{kind}.png")
    for kind in ["absolute", "normalized"]
}
PATH_BOXWHISKER = str(DIR_FIGS / "{dr}" / "SCISM_allSSPIAM_slrAR6_boxplot_optimal.png")

# Make directories where needed
for p in [
    DIR_SCRATCH,
    DIR_FIGS,
]:
    p.mkdir(exist_ok=True, parents=True)


def start_dask_cluster(n_workers=8):
    """Instantiate dask distributed client and cluster.

    Code Ocean capsules run on 16-core machines by default. This function can be changed
    to match your specs if running elsewhere.
    """
    client = Client(n_workers=n_workers)
    cluster = client.cluster
    return client, cluster
