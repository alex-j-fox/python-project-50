install:
	poetry install

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest
	
verbose-test:
	poetry run pytest -vv
	
test-coverage:
	poetry run pytest --cov=gendiff --cov-report=xml

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install build publish package-install lint test verbose-test test-coverage selfcheck check