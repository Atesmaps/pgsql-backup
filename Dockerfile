FROM python:3.12

ENV DEBIAN_FRONTEND=noninteractive
ENV PROJECT_DIR=/usr/local/src/pgsql-backup
WORKDIR ${PROJECT_DIR}

RUN apt-get update \
    && apt-get dist-upgrade -y \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

COPY Pipfile* ${PROJECT_DIR}/

RUN pipenv install --system --deploy

COPY src ${PROJECT_DIR}/

ENTRYPOINT ["/usr/local/bin/python"]
CMD ["main.py"]
