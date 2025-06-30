FROM registry.codeocean.com/codeocean/py-r:python3.12.8-R4.4.2-JupyterLab4.3.5-RStudiorstudio-server-2024.12.1-563-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

COPY environment.yml /

RUN conda install conda=25 && \
    conda env update -n base -f=/environment.yml && \
    conda update --all && \
    conda clean -ya

ENV DASK_LABEXTENSION__DEFAULT__WORKERS=16
ENV DASK_DISTRIBUTED__DASHBOARD__LINK="proxy/{port}/status"
ENV DASK_DISTRIBUTED__WORKER__MEMORY__SPILL=0.98
ENV DASK_DISTRIBUTED__WORKER__MEMORY__PAUSE=0.98
ENV DASK_DISTRIBUTED__WORKER__MEMORY__TERMINATE=0.99
ENV PROJ_LIB=/opt/conda/share/proj

COPY download-input-data.py postInstall /
# RUN /postInstall