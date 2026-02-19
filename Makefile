.DEFAULT_GOAL := help

SHELL := /bin/bash

POETRY ?= poetry
PYTEST ?= $(POETRY) run pytest
DOCKER_COMPOSE ?= docker compose
ENV_FILE ?= .env.test

.PHONY: help
help:
	@echo ""
	@echo "Targets:"
	@echo "  make install            Install dependencies (poetry)"
	@echo "  make lint               Run ruff lint (no fixes)"
	@echo "  make lint-fix           Run ruff lint (with fixes)"
	@echo "  make format             Run ruff formatter"
	@echo "  make test-unit          Run unit tests (with coverage)"
	@echo "  make test-integration   Run integration tests (no coverage)"
	@echo "  make docker-build       Build test image"
	@echo "  make docker-integration Run integration via docker-compose"
	@echo "  make clean              Remove caches/reports"
	@echo ""

.PHONY: install
install:
	$(POETRY) install --no-interaction --no-ansi

.PHONY: lint
lint:
	$(POETRY) run task lint

.PHONY: lint-fix
lint-fix:
	$(POETRY) run task check

.PHONY: format
format:
	$(POETRY) run task format

.PHONY: test-unit
test-unit:
	$(POETRY) run task test_unit

.PHONY: test-integration
test-integration:
	$(POETRY) run task test_integration

.PHONY: docker-build
docker-build:
	docker build -t hub-automation-integration-api:latest .

.PHONY: docker-integration
docker-integration:
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) up --build --abort-on-container-exit

.PHONY: clean
clean:
	rm -rf .pytest_cache .ruff_cache .mypy_cache htmlcov reports __pycache__
	rm -f .coverage .coverage.*

