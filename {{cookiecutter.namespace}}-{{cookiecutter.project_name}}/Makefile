.PHONY: help lint/full lint/fix lint init build test test/full
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
        match = re.match(r'^([\/a-zA-Z_-]+):.*?## (.*)$$', line)
        if match:
                target, help = match.groups()
                print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help: ## show help
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

lint/full: ## complex check of the code
	@poetry run cruft check
	@poetry run ruff {{cookiecutter.namespace}}/{{cookiecutter.project_slug}}
	@poetry run isort --check --diff {{cookiecutter.namespace}}/{{cookiecutter.project_slug}}
	@poetry run bandit -r  {{cookiecutter.namespace}}/{{cookiecutter.project_slug}}
	@poetry run safety check -i 53269 -i 47794
	@poetry run mypy --ignore-missing-imports {{cookiecutter.namespace}}

lint/fix: ## automatic code fix       
	@poetry run isort {{cookiecutter.namespace}}/{{cookiecutter.project_slug}}
	@poetry run ruff --fix {{cookiecutter.namespace}}/{{cookiecutter.project_slug}}

lint: ## fast check of lint
	@poetry run ruff {{cookiecutter.namespace}}/{{cookiecutter.project_slug}} tests/

init: install/precommit ## init development eviroment
	@pip install -U poetry tox
	@poetry install
 
install/precommit: ## install commitizef ro checking commits
	@pip install -U commitizen pre-commit
	@pre-commit install --hook-type commit-msg --hook-type pre-push

build: ## build package
	@poetry build

test: ## run python tests with coverage report
	@poetry run pytest -s --cov={{cookiecutter.namespace}}/{{cookiecutter.project_slug}} --cov=tests --cov-report=term-missing tests --cov-report html

test/full: ## run tox tests
	tox
