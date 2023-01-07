.PHONY: clean \
	setup \
	setup-db \
	secrets \
	test \
	test-coverage \

DIRENV_BINARY := $(shell command -v direnv 2> /dev/null)
WAIT_TIME_FOR_DB := 10

help:
	@echo "make"
	@echo "    clean"
	@echo "        Remove Python/build artifacts."
	@echo "    setup"
	@echo "        Setup carnage configuration files."
	@echo "    setup-db"
	@echo "        Setup carnage database."
	@echo "    test"
	@echo "        Run pytest on tests/."
	@echo "    test-coverage"
	@echo "        Run pytest with tox on tests/."

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	find . -name '.coverage' -exec rm -f  {} +
	find . -name 'coverage.xml' -exec rm -f  {} +
	rm -rf build/
	rm -rf .mypy_cache/
	rm -rf dist/
	rm -rf docs/build
	rm -rf .tox
	rm -rf .ruff_cache

setup:
ifneq ($(shell test -s .env && echo -n yes),yes)
	cp .env.example .env
ifdef DIRENV_BINARY
	direnv reload
endif
endif

secrets: clean
	python scripts/generate_secrets.py

setup-db: setup
	@docker-compose down
	docker-compose up -d database
	@echo "Waiting $(WAIT_TIME_FOR_DB) to run migrations"
	@sleep $(WAIT_TIME_FOR_DB)
	alembic upgrade heads
	carnage --debug seed --all

test: setup
	pytest tests

test-coverage: setup
	tox
	coverage html
