#!/usr/bin/env bash
set -ex

# This is the master script for the capsule. When you click "Reproducible Run", the code in this file will execute.

run_nb() {
    NBPATH=/code/$1.ipynb
    OUTPATH=${NBPATH/"code"/"results/notebook-output"}
    mkdir -p $(dirname "$OUTPATH")
    shift
    papermill $NBPATH $OUTPATH \
        --cwd $(dirname "$NBPATH") \
        "$@"
}

run_nb 1-combine-slr-data

run_nb 2-collapse-sliiders-to-seg

# these intermediate data files take awhile to create and thus are included in the capsule as pre-generated data.
# you may run this script to re-create them if you wish
# papermill 3-create-surge-lookup-tables.ipynb

run_nb 4-run-pyCIAM

run_nb 5-generate-manuscript-content -p DR 0.015
run_nb 5-generate-manuscript-content -p DR 0.02
run_nb 5-generate-manuscript-content -p DR 0.03
