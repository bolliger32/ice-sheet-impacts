# Quantifying Asymmetries in Flood Area and Population Exposure Between Sea Level Fingerprints of Melting From the Antarctic and Greenland Ice Sheets
A comparative analysis of the societal impacts of Greenland and Antarctic Ice Sheet mass flux. This code is associated with the manuscript "Quantifying Asymmetries in Flood Area and Population Exposure Between Sea Level Fingerprints of Melting From the Antarctic and Greenland Ice Sheets" (Bolliger et al., submitted). It is part of a Code Ocean capsule

This repository provides the code required to produce the figures appearing in the main text and Supplementary Materials of:

Bolliger et al., ""Quantifying Asymmetries in Flood Area and Population Exposure Between Sea Level Fingerprints of Melting From the Antarctic and Greenland Ice Sheets," *Under Review*.

If you are viewing this repository on Github, please see our Code Ocean capsule, where you will find a mirror of this repository along with data and a computing environment set up to execute the analysis. You may interact with the code via this platform or simply download the data for use on your own platform.

## Installation

The easiest way to replicate and/or interact with our analysis is to use this Code Ocean capsule, which provides a cloud platform containing our code, data, and computing environment together. An alternative approach is to separately obtain these three items for use on an alternative computing platform.

To reproduce the analyses in the associated paper via Code Ocean, you will likely want to use the `Launch Cloud Workstation-->JupyterLab` functionality.

If you choose to replicate the analysis on a different platform, you will separately need to obtain three things: code, data, and an appropriate computing environment:

#### Code

You should clone this repository, which is mirrored on [Github](https://github.com/bolliger32/ice-sheet-impacts) and Code Ocean. Either source is appropriate to clone as they contain the same code. You may need to modify some of the filepaths in [shared.py](code/shared.py) to reflect the location of data on your local machine if you modify it from the default location (see below).

#### Data

When viewing our Code Ocean capsule, hover over `data` and click the caret that appears. You will see an option to download this folder. Place this downloaded `data` folder in the root directory of this repository (i.e. at the same level as the `code/` folder). Alternatively, you may place a symlink at that location that points to this data folder.

##### Data Description

The following 

#### Computing Environment

You will need to install and activate our [conda](https://docs.conda.io/en/latest/miniconda.html) environment. Once you have conda installed on your machine, from the root directory of this repository, run:

```bash
conda env create -f environment/environment.yml -n ice-sheets
conda activate ice-sheets
```

If you would instead like to execute this code within a Docker container, you may use the [Dockerfile](environment/Dockerfile). However, you will need to replace the base image with the commented out one in order to access the public version of this base image rather than the one hosted on Code Ocean's registry.

## Use of code and data

Our code can be used, modified, and distributed freely for educational, research, and not-for-profit uses. For all other cases, please contact us. Further details are available in the [code license](code/LICENSE). All data products created through our work that are not covered under upstream licensing agreements are available via a CC BY-NC license (see the [data license](data/LICENSE) available within the Code Ocean capsule). All upstream data use restrictions take precedence over this license.
