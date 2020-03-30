FROM python:3.8-alpine AS builder

ENV PATH="/opt/venv/bin:$PATH"
ENV PIP_DISABLE_PIP_VERSION_CHECK="1"
ENV PIP_NO_CACHE_DIR="1"
COPY ./ /cephadm-ansible

RUN apt --no-cache add --update build-base
RUN python -m venv /opt/venv

#
# Production
#

FROM builder AS production
RUN pip install --no-cache-dir \
    -r /cephadm-ansible/requirements.txt

#
# Staging
#

FROM builder AS staging
RUN pip install --no-cache-dir \
    -r /cephadm-ansible/requirements.dev.txt
