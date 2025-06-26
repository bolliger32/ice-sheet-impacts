#!/usr/bin/env python3

"""Download raw data needed for analysis.

All downloads executed in this script are contained in the data/raw folder in the Code Ocean
capsule. Thus, this script is included for transparency but does not need to be executed as part
of the capsule.
"""

import requests
import shared
from cloudpathlib import AnyPath
from fsspec.implementations.libarchive import LibArchiveFileSystem
from pyCIAM.io import (
    download_and_extract_from_zenodo,
    download_and_extract_partial_zip,
)

# ##############
# ZENODO SOURCES
# ##############

Z_URL_RECORDS = "https://zenodo.org/api/records/{doi}"
Z_SLIIDERS_DOI = "10714387"
Z_AR6_DOI = "6382554"
Z_WANG_SUN_DOI = "7898409"

# #########
# DOWNLOADS
# #########

# download Wang and Sun
with LibArchiveFileSystem(
    "https://zenodo.org/records/7898409/files/GDP_2010-2010.7z"
).open("GDP_2010-2010/GDP2020.tif", "rb") as file:
    shared.PATH_GRIDDED_GDP.write_bytes(file.read())

# download SLIIDERS
sliiders_files = requests.get(Z_URL_RECORDS.format(doi=Z_SLIIDERS_DOI)).json()["files"]
download_and_extract_from_zenodo(
    AnyPath(shared.PATH_SLIIDERS), sliiders_files, "sliiders-v"
)

# download AR6 SLR data
ar6_files = requests.get(Z_URL_RECORDS.format(doi=Z_AR6_DOI)).json()["files"]

# get total SLR
for scope, name in [("global", "ar6"), ("regional", "ar6-regional-confidence")]:
    print(f"Downloading AR6 SLR projections: total, {scope}...")
    download_and_extract_from_zenodo(
        shared.DIR_SLR_AR6_RAW / scope,
        ar6_files,
        f"{name}.zip",
        zip_glob=(f"{name}/{scope}/confidence_output_files/**/ssp*/total_*values.nc"),
    )

# get only the contribution of vertical land motion
print("Downloading AR6 SLR projections: verticallandmotion, regional...")
download_and_extract_from_zenodo(
    shared.DIR_SLR_AR6_RAW / "regional",
    ar6_files,
    "ar6-regional-confidence.zip",
    zip_glob=(
        "ar6-regional-confidence/regional/confidence_output_files/**/ssp*/"
        "verticallandmotion_*values.nc"
    ),
)

# download GADM
if not shared.PATH_GADM.is_file():
    GADM_NAME = shared.PATH_GADM.stem
    download_and_extract_partial_zip(
        shared.PATH_GADM.parent,
        f"https://geodata.ucdavis.edu/gadm/gadm4.1/{GADM_NAME}.zip",
        f"{GADM_NAME}.gpkg",
    )
