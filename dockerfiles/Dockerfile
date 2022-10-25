FROM python:3.11-slim as base

ENV DEBIAN_FRONTEND="noninteractive"

# make sure we use the virtualenv
ENV PATH="/opt/venv/bin:$PATH"

FROM base as build

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /build

COPY ["./pyproject.toml", "./poetry.lock", "./LICENSE", "./README.md", "/build/"]
ADD carnage /build/carnage

RUN apt update -y \
    && apt install curl --no-install-recommends -y \
    && curl -sSL https://install.python-poetry.org/ | python \
    && python -m venv /opt/venv \
    && . /opt/venv/bin/activate && poetry install --no-dev --no-root --no-interaction \
    && . /opt/venv/bin/activate && poetry build -f wheel -n \
    && . /opt/venv/bin/activate && pip install --no-deps dist/carnage*.whl \
    && rm -rf dist *.egg-info

FROM base as runner

COPY --from=build /opt/venv /opt/venv

RUN useradd -rm -d /carnage -s /sbin/nologin -g root -u 1001 carnage && groupadd -g 1001 carnage

ENTRYPOINT ["carnage", "serve"]
