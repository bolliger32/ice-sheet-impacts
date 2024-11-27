# Quantifying Asymmetries in Flood Area and Population Exposure Between Sea Level Fingerprints of Melting From the Antarctic and Greenland Ice Sheets

This repository provides the code required to produce the figures appearing in the main text and Supplementary Materials of:

Bolliger et al., "Quantifying Asymmetries in Flood Area and Population Exposure Between Sea Level Fingerprints of Melting From the Antarctic and Greenland Ice Sheets," *Under Review*.

If you are viewing this repository on Github, please also see our Code Ocean capsule [ADD LINK], where you will find a mirror of this repository along with data and a computing environment set up to execute the analysis. You may interact with the code via this platform or simply download the data for use on your own platform.

## Installation

The easiest way to replicate and/or interact with our analysis is to use this Code Ocean capsule, which provides a cloud platform containing our code, data, and computing environment together. An alternative approach is to separately obtain these three items for use on an alternative computing platform.

To reproduce the analyses in the associated paper via Code Ocean, you will likely want to use the `Launch Cloud Workstation-->JupyterLab` functionality.

If you choose to replicate the analysis on a different platform, you will separately need to obtain three things: code, data, and an appropriate computing environment:

## Code

You should clone this repository, which is mirrored on [Github](https://github.com/bolliger32/ice-sheet-impacts) and Code Ocean. Either source is appropriate to clone as they contain the same code. You may need to modify some of the filepaths in [shared.py](code/shared.py) to reflect the location of data on your local machine if you modify it from the default location (see below).

## Data

When viewing our Code Ocean capsule, hover over `data` and click the caret that appears. You will see an option to download this folder. Place this downloaded `data` folder in the root directory of this repository (i.e. at the same level as the `code/` folder). Alternatively, you may place a symlink at that location that points to this data folder. Alternatively, the [download-input-data.py](environment/download-input-data.py) script will download the majority of these files. The LANDSCAN dataset requires non-programmatic (point-and-click) downloads, while [ypk_2000_2020_20240222.parquet](data/raw/ypk_2000_2020_20240222.parquet) and [ice-sheet-contributions.parquet](data/raw/ice-sheet-contributions.parquet) are not otherwise publicly available and must be downloaded from the Code Ocean capsule.

### Data Description

The following files are included in the Code Ocean capsule under [data/raw](data/raw) and are needed to execute the analysis (links will work only on the Code Ocean capsule):

* [sliiders-v1.2.zarr](data/raw/sliiders-v1.2.zarr): The Sea Level Rise Impacts Input Dataset by Region, Elevation, and Scenario ([Depsky et al., 2023, Bolliger et al., 2023](https://zenodo.org/records/10779331))
* [ypk_2000_2020_20240222.parquet](data/raw/ypk_2000_2020_20240222.parquet): An intermediate file created in the process of generating SLIIDERS (see the [SLIIDERS github repo](https://github.com/ClimateImpactLab/sliiders/blob/main/notebooks/data-processing/1-country-level-temporal-trends/1-historical-income-pop.ipynb)). It contains country-year level estimates of GDP and population, aggregated from numerous sources, primarily [Penn World Table v10.01](https://www.rug.nl/ggdc/productivity/pwt/).
* [wang_and_sun_2020_gdp.zarr](data/raw/wang_and_sun_2020_gdp.zarr): 2020 estimates of gridded GDP estimates from [Wang and Sun, 2020](https://www.nature.com/articles/s41597-022-01300-x) ([Zenodo deposit, v7](https://zenodo.org/records/7898409))
* [ice-sheet-contributions.parquet](data/raw/ice-sheet-contributions.parquet): Estimates of local sea level rise at each SLIIDERS segment associated with 1 cm of global SLR, pre-computed using the outputs of [Cederberg et al., 2023](https://academic.oup.com/gji/article/235/1/353/7188292?login=false) ([Zenodo deposit](https://zenodo.org/records/7949464))
* [gadm_410-levels.gpkg](data/raw/gadm_410-levels.gpkg). State/province-level administrative boundaries from the [GADM dataset](https://gadm.org) (consistent with the boundaries used in the creation of SLIIDERS).
* [landscan-global-2020.tif](data/raw/landscan-global-2020.tif): The 2020 release of global gridded population estimates from [LANDSCAN](https://landscan.ornl.gov).

### Computing Environment

You will need to install and activate our [conda](https://docs.conda.io/en/latest/miniconda.html) environment. Once you have conda installed on your machine, from the root directory of this repository, run:

```bash
conda env create -f environment/environment.yml -n ice-sheets
conda activate ice-sheets
```

If you would instead like to execute this code within a Docker container, you may use the [Dockerfile](environment/Dockerfile). However, you will need to replace the base image with the commented out one in order to access the public version of this base image rather than the one hosted on Code Ocean's registry.

## Outputs

Consistent with the Code Ocean capsule structure, this repo is designed to output figures used in Bolliger et al. (2023) in a `results/figures` folder, relative to the root directory.

## Use of code and data

Our code can be used, modified, and distributed freely for educational, research, and not-for-profit uses. For all other cases, please contact us. Further details are available in the [code license](code/LICENSE). All data products created through our work that are not covered under upstream licensing agreements are available via a CC BY-NC license (see the [data license](data/LICENSE) available within the Code Ocean capsule). All upstream data use restrictions take precedence over this license.
