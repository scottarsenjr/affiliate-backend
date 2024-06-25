ifeq ($(OS),Windows_NT)
    MANAGE_PY := poetry run python -m core.manage
else
    MANAGE_PY := poetry run python3.11 -m core.manage
endif

# Project Setup/Managing commands
.PHONY: install
install:
	poetry install

.PHONY: copy-template
copy-template:
	cp ./core/project/settings/templates/settings.dev.py ./local/settings.dev.py
	cp ./core/project/settings/templates/settings.prod.py ./local/settings.prod.py

.PHONY: pre-commit-uninstall
pre-commit-uninstall:
	poetry run pre-commit uninstall

.PHONY: pre-commit-install
pre-commit-install:
	poetry run pre-commit install

.PHONY: install-pre-commit
update-pre-commit: pre-commit-uninstall pre-commit-install;

.PHONY: migrate
migrate:
	poetry run $(MANAGE_PY) migrate

.PHONY: migrations
migrations:
	poetry run $(MANAGE_PY) makemigrations

.PHONY: superuser
superuser:
	poetry run $(MANAGE_PY) createsuperuser

.PHONY: run-server
run-server:
	poetry run $(MANAGE_PY) runserver

.PHONY: run-celery
run-celery:
	poetry run celery -A core.project worker -l info

.PHONY: run-celery-beat
run-celery-beat:
	poetry run celery -A core.project beat -l info

.PHONY: update
update:
	install migrate update-pre-commit

# Prevent make from interpreting the argument as a make target
%:
	@:
