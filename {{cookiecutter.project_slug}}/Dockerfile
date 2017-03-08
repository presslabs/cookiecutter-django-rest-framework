FROM python:3.5-alpine

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=django_project.settings

COPY ./requirements.txt /requirements.txt
RUN set -ex \
    && apk add --no-cache \
        make \
        mariadb-client-libs \
        openssl \
        su-exec \
    && addgroup -g 998 {{ cookiecutter.project_slug }} \
    && adduser -SD -u 998 -G {{ cookiecutter.project_slug }} -h /app {{ cookiecutter.project_slug }} \
    && apk add --no-cache --virtual .build-deps \
        build-base \
        mariadb-dev \
    && pip install --no-cache-dir -r /requirements.txt \
    && apk del .build-deps

COPY . /app
WORKDIR /app

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["web"]
