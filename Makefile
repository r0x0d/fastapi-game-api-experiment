.PHONY: clean setup setup-db test test-coverage

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
	rm -rf build/
	rm -rf .mypy_cache/
	rm -rf dist/
	rm -rf docs/build

setup:
ifneq ($(shell test -s .env && echo -n yes),yes)
	cp .env.example .env
ifdef DIRENV_BINARY
	direnv reload
endif
endif

setup-db: setup
	docker-compose up -d database
	@echo "Waiting $(WAIT_TIME_FOR_DB) to run migrations"
	@sleep $(WAIT_TIME_FOR_DB)
	carnage migration
	carnage seed --all

test: setup clean
	pytest tests

test-coverage: setup clean
	tox
	coverage html
