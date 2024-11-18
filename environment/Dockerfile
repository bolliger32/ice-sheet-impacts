# hash:sha256:fd1cdbc90bcdb699cccb7aa23aa052376644f6b1cfa7a9be556ef32747275f8d
FROM registry.codeocean.com/codeocean/mambaforge3:22.11.1-4-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN conda update --all -y && \
    conda install conda=24 && \
    conda install python=3.12 && \
    conda update --all && \
    conda install -y \
        bottleneck \
        cachey \
        cartopy \
        cloudpathlib \
        dask-expr \
        dask-labextension \
        distributed \
        flox \
        gitpython \
        ipywidgets \
        jupyterlab \
        lz4 \
        matplotlib \
        netcdf4 \
        numbagg \
        opt_einsum \
        papermill \
        pint-xarray \
        psutil \
        pyarrow \
        python-snappy \
        scikit-learn \
        xarray \
        zarr && \
    conda clean -ya

RUN pwd
RUN pip install --src /pyciam --no-cache-dir -e \
    git+https://github.com/ClimateImpactLab/pyCIAM@bugfix/more-dep-fixes#egg=python-ciam

COPY postInstall /
RUN /postInstall

ENV DASK_LABEXTENSION__DEFAULT__WORKERS=16
ENV DASK_DISTRIBUTED__DASHBOARD__LINK="{JUPYTERHUB_SERVICE_PREFIX}proxy/{port}/status"
ENV DASK_DISTRIBUTED__WORKER__MEMORY__SPILL=0.98
ENV DASK_DISTRIBUTED__WORKER__MEMORY__PAUSE=0.98
ENV DASK_DISTRIBUTED__WORKER__MEMORY__TERMINATE=0.99