.DEFAULT_GOAL := build

test:
	py.test -v --flake8
full-test:
	py.test -v --color=yes
lint:
	py.test -v --color=yes --flake8 -m 'flake8'
run:
	@echo "*** Run 'celery worker -A django_project -B' in order to start the background worker ***"
	python ./manage.py runserver
build:
	@echo "There is nothing to build for this project"
seed:
	python ./manage.py migrate --no-input
	python ./manage.py seed
.PHONY: test full-test run build lint seed
