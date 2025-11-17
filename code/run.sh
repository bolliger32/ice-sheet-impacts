#!/usr/bin/env bash
set -ex

# This is the master script for the capsule. When you click "Reproducible Run", the code in this file will execute.

run_nb() {
    NBPATH=/code/$1.ipynb
    OUTPATH=/results/notebook-output/$2/$1.ipynb
    mkdir -p $(dirname "$OUTPATH")
    shift
    papermill $NBPATH $OUTPATH \
        --cwd $(dirname "$NBPATH") \
        "$1"
}

run_nb 1-combine-slr-data data-processing

run_nb 2-collapse-sliiders-to-seg data-processing

# these intermediate data files take awhile to create and thus are included in the capsule as pre-generated data.
# you may run this script to re-create them if you wish
# papermill 3-create-surge-lookup-tables.ipynb

run_nb 4-run-pyCIAM model-execution

run_nb 5-generate-manuscript-content figs/dr_15 -p DR 0.015
run_nb 5-generate-manuscript-content figs/dr_2 -p DR 0.02
run_nb 5-generate-manuscript-content figs/dr_3 -p DR 0.03

run_nb 6-gen-fig1 figs
