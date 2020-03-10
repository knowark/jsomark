clean:
	find . -name '*.pyc' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +
	find . -name '.mypy_cache' -exec rm -fr {} +
	find . -name 'pip-wheel-metadata' -exec rm -fr {} +
	find . -name 'jsomark.egg-info' -exec rm -fr {} +

test:
	pytest

COVFILE ?= .coverage

coverage: 
	export COVERAGE_FILE=$(COVFILE); pytest -x --cov=jsomark tests/ \
	--cov-report term-missing -vv -s -o cache_dir=/tmp/.pytest_cache

PART ?= patch

version:
	bump2version $(PART) pyproject.toml jsomark/__init__.py --tag --commit
