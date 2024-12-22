#!/usr/bin/env bash
set -ex

# This is the master script for the capsule. When you click "Reproducible Run", the code in this file will execute.

run_nb() {
    NBPATH=$1
    OUTPATH=${NBPATH/"code"/"results/notebook-output"}
    mkdir -p $(dirname "$OUTPATH")
    shift
    papermill $NBPATH $OUTPATH \
        --cwd $(dirname "$NBPATH") \
        "$@"
}

run_nb /code/1-combine-slr-data.ipynb

run_nb /code/2-collapse-sliiders-to-seg.ipynb

# these intermediate data files take awhile to create and thus are included in the capsule as pre-generated data.
# you may run this script to re-create them if you wish
# papermill 3-create-surge-lookup-tables.ipynb

run_nb /code/4-run-pyCIAM.ipynb

run_nb /code/5-generate-manuscript-content.ipynb -p DPI 300 -p PLOT_TEXT False
