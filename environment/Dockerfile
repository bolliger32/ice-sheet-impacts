# hash:sha256:fd1cdbc90bcdb699cccb7aa23aa052376644f6b1cfa7a9be556ef32747275f8d
FROM registry.codeocean.com/codeocean/mambaforge3:22.11.1-4-ubuntu22.04
# FROM condaforge/mambaforge:22.11.1-4

ARG DEBIAN_FRONTEND=noninteractive

COPY environment.yml /

RUN conda update --all -y && \
    conda install conda=24 && \
    conda install python=3.12 && \
    conda update --all && \
    conda env update -n base -f=/environment.yml && \
    conda clean -ya

RUN pwd
RUN pip install --src / --no-cache-dir -e \
    git+https://github.com/ClimateImpactLab/pyCIAM@bugfix/more-dep-fixes#egg=python-ciam

ENV DASK_LABEXTENSION__DEFAULT__WORKERS=16
ENV DASK_DISTRIBUTED__DASHBOARD__LINK="proxy/{port}/status"
ENV DASK_DISTRIBUTED__WORKER__MEMORY__SPILL=0.98
ENV DASK_DISTRIBUTED__WORKER__MEMORY__PAUSE=0.98
ENV DASK_DISTRIBUTED__WORKER__MEMORY__TERMINATE=0.99
ENV PROJ_LIB=/opt/conda/share/proj

COPY download-input-data.py postInstall /
# RUN /postInstall