FROM python:3.10-slim as base

# Setup env
# ENV LANG C.UTF-8
# ENV LC_ALL C.UTF-8
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONFAULTHANDLER 1
# ENV SECRET_KEY KEY

FROM base AS python-deps

# Install pipenv and compilation dependencies
RUN pip install pipenv

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Change shell
RUN ln -sf /bin/bash /bin/sh

# Create and switch to a new user
RUN useradd --create-home logat-mesir-backend
WORKDIR /home/logat-mesir-backend
USER logat-mesir-backend

# Install application into container
COPY . .