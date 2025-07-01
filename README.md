# Quantifying Asymmetries in Flood Area and Population Exposure Between Sea Level Fingerprints of Mass Loss from the Antarctic and Greenland Ice Sheets

This repository provides the code required to produce Figure 1 along with the economic analysis figures (Figures 5-7 and S5-S12), as well as a variety of quantities referenced in the main text, for:

Bolliger et al., "Quantifying Asymmetries in Flood Area and Population Exposure Between Sea Level Fingerprints of Melting From the Antarctic and Greenland Ice Sheets," *Authorea*. January 27, 2025. 10.22541/au.173801314.47840038/v1.

If you are viewing this repository on Github, please also see our Code Ocean capsule (link coming soon), where you will find a mirror of this repository along with data and a computing environment set up to execute the analysis. You may interact with the code via this platform or simply download the data for use on your own platform.

Code and data associated with all other figures and quantities in the manuscript are located at [https://doi.org/10.5281/zenodo.14567046](https://doi.org/10.5281/zenodo.14567046). The remainder of this README will focus on the analysis included in this repository, while you may find separate instructions for replicating the rest of the study at the aforementioned DOI.

## Installation

The easiest way to replicate and/or interact with our analysis is to use this Code Ocean capsule, which provides a cloud platform containing our code, data, and computing environment together. An alternative approach is to separately obtain these three items for use on an alternative computing platform.

To reproduce the analyses in the associated paper via Code Ocean, you will likely want to use the `Launch Cloud Workstation-->JupyterLab` functionality.

If you choose to replicate the analysis on a different platform, you will separately need to obtain three things: code, data, and an appropriate computing environment:

### Code

You should clone this repository, which is mirrored on [Github](https://github.com/bolliger32/ice-sheet-impacts) and Code Ocean. Either source is appropriate to clone as they contain the same code. You may need to modify some of the filepaths in [shared.py](code/shared.py) to reflect the location of data on your local machine if you modify it from the default location (see below).

### Data

When viewing our Code Ocean capsule, hover over `data` and click the caret that appears. You will see an option to download this folder. Place this downloaded `data` folder in the root directory of this repository (i.e. at the same level as the `code/` folder). Alternatively, you may place a symlink at that location that points to this data folder. Alternatively, the [download-input-data.py](environment/download-input-data.py) script will download the majority of these files. Non-programmatic downloads include:

* [landscan-global-2020.tif](data/raw/landscan-global-2020.tif): The LANDSCAN dataset requires non-programmatic (point-and-click) downloads
* [ypk_2000_2020_20240222.parquet](data/raw/ypk_2000_2020_20240222.parquet) is an intermediate output in the creation of the [SLIIDERS dataset, v1.2](https://doi.org/10.5194/gmd-16-4331-2023) ([Github](https://github.com/ClimateImpactLab/sliiders)). It is replicable through the steps included in that repository but is not otherwise available on the public [Zenodo upload](https://doi.org/10.5281/zenodo.10779331).
* [ice-sheet-contributions.parquet](data/raw/ice-sheet-contributions.parquet) contains a reformatted table of a single fingerprint for both AIS and GrIS, scaled such that the GMSL for each is 1cm. This is used to apply a sea level "delta" with which to calculate the SC-ISM. Calculations for this file are contained in the companion [Zenodo upload for this manuscript](https://doi.org/10.5281/zenodo.14567046).
* [surge-lookup-v1.2-seg_adm.zarr](data/int/surge-lookup-v1.2-seg_adm.zarr) and [surge-lookup-v1.2-seg.zarr](data/int/surge-lookup-v1.2-seg.zarr) take a reasonably long time to compute and are pre-computed for our Code Ocean capsule. Should you wish to not re-calculate these files, you will also need to download those.
* [sea_ant86.txt](data/raw/slr/sea_ant86.txt) and [sea_green44.txt](data/raw/slr/sea_green44.txt) are example SLR fingerprints derived from those contained in [Cederberg et al., 2023](https://doi.org/10.1093/gji/ggad214) ([Zenodo upload](https://doi.org/10.5281/zenodo.7949464)). They have been preprocessed for ease of plotting in Figure 1.

#### Data Description

The following files are included in the Code Ocean capsule under [data/raw](data/raw) and are needed to execute the analysis (links will work only on the Code Ocean capsule):

* [sliiders-v1.2.zarr](data/raw/sliiders-v1.2.zarr): The Sea Level Rise Impacts Input Dataset by Region, Elevation, and Scenario ([Depsky et al., 2023, Bolliger et al., 2023](https://zenodo.org/records/10779331))
* [ypk_2000_2020_20240222.parquet](data/raw/ypk_2000_2020_20240222.parquet): An intermediate file created in the process of generating SLIIDERS (see the [SLIIDERS github repo](https://github.com/ClimateImpactLab/sliiders/blob/main/notebooks/data-processing/1-country-level-temporal-trends/1-historical-income-pop.ipynb)). It contains country-year level estimates of GDP and population, aggregated from numerous sources, primarily [Penn World Table v10.01](https://www.rug.nl/ggdc/productivity/pwt/).
* [wang_and_sun_2020_gdp.tif](data/raw/wang_and_sun_2020_gdp.tif): 2020 estimates of gridded GDP estimates from [Wang and Sun, 2020](https://www.nature.com/articles/s41597-022-01300-x) ([Zenodo upload, v7](https://zenodo.org/records/7898409))
* [gadm_410-levels.gpkg](data/raw/gadm_410-levels.gpkg). State/province-level administrative boundaries from the [GADM dataset](https://gadm.org) (consistent with the boundaries used in the creation of SLIIDERS).
* [landscan-global-2020.tif](data/raw/landscan-global-2020.tif): The 2020 release of global gridded population estimates from [LANDSCAN](https://landscan.ornl.gov).
* [ice-sheet-contributions.parquet](data/raw/slr/ice-sheet-contributions.parquet): Estimates of local sea level rise at each SLIIDERS segment associated with 1 cm of global SLR, pre-computed using the outputs of [Cederberg et al., 2023](https://academic.oup.com/gji/article/235/1/353/7188292?login=false) ([Zenodo upload](https://zenodo.org/records/7949464))
* [ar6](data/raw/slr/ar6): A collection of sea level rise projections from the [Framework for Assessing Changes To Sea-level (FACTS)](https://doi.org/10.5194/gmd-16-7461-2023) ([Zenodo upload](https://doi.org/10.5281/zenodo.6382554)). Not all files from the Zenodo upload are needed. See [download-input-data.py](environment/download-input-data.py) for a script to download the necessary projection files.
* [sea_ant86.txt](data/raw/slr/sea_ant86.txt): An example SLR fingerprint from Antarctic Ice Sheet melt, as modeled in [Cederberg et al., 2023](https://doi.org/10.1093/gji/ggad214) ([Zenodo upload](https://doi.org/10.5281/zenodo.7949464)).
* [sea_green44.txt](data/raw/slr/sea_green44.txt): An example SLR fingerprint from Greenland Ice Sheet melt, as modeled in [Cederberg et al., 2023](https://doi.org/10.1093/gji/ggad214) ([Zenodo upload](https://doi.org/10.5281/zenodo.7949464)).

### Computing Environment

You will need to install and activate our [conda](https://docs.conda.io/en/latest/miniconda.html) environment. Once you have conda installed on your machine, from the root directory of this repository, run:

```bash
conda env create -f environment/environment.yml -n ice-sheets
conda activate ice-sheets
```

If you would instead like to execute this code within a Docker container, you may use the [Dockerfile](environment/Dockerfile). However, you will need to replace the base image with the commented out one in order to access the public version of this base image rather than the one hosted on Code Ocean's registry.

## Outputs

Consistent with the Code Ocean capsule structure, this repo is designed to output figures in a `results/figures` folder, relative to the root directory.

## Use of code and data

Our code can be used, modified, and distributed freely for educational, research, and not-for-profit uses. For all other cases, please contact us. Further details are available in the [code license](code/LICENSE). All data products created through our work that are not covered under upstream licensing agreements are available via a CC BY-NC license (see the [data license](data/LICENSE) available within the Code Ocean capsule). All upstream data use restrictions take precedence over this license.
