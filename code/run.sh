#!/usr/bin/env bash
set -ex

# This is the master script for the capsule. When you click "Reproducible Run", the code in this file will execute.
bash run.sh "$@"

papermill 1-combine-slr-data.ipynb

papermill 2-collapse-sliiders-to-seg.ipynb

# these intermediate data files take awhile to create and thus are included in the capsule as pre-generated data.
# you may run this script to re-create them if you wish
# papermill 3-create-surge-lookup-tables.ipynb

papermill 4-run-pyCIAM.ipynb

papermill 5-generate-manuscript-content.ipynb -p DPI=300
