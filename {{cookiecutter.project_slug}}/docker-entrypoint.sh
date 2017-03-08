#!/bin/sh
set -eo pipefail

LOG_LEVEL=${% raw %}{{% endraw %}{{ cookiecutter.project_env_prefix }}_LOG_LEVEL:-INFO{% raw %}}{% endraw %}

case "$1" in
    "web")         exec su-exec {{ cookiecutter.project_slug }} gunicorn django_project.wsgi --bind 0.0.0.0:8000;;
    "celery")      exec su-exec {{ cookiecutter.project_slug }} celery -A django_project worker;;
    "beat")        exec su-exec {{ cookiecutter.project_slug }} celery -A django_project beat;;
esac

exec "$@"
