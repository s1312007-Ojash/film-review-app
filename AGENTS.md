# AGENTS.md

This file provides guidance to AI coding agents (including Claude Code at claude.ai/code) when working with code in this repository.

## Project state

A Django 6 / Python 3.14 web app for browsing films, reading/writing reviews, star ratings (0–5), and saving favorites. **Currently a fresh skeleton**: `config/` holds the project, but none of the domain apps (films, reviews, accounts) described in the README exist yet. Building a feature generally means creating a new Django app, wiring it into `INSTALLED_APPS` and `config/urls.py`, and adding migrations.

## Commands

Everything runs through `uv` (manages the venv and the lockfile — don't invoke `python`/`pip` directly):

```bash
uv sync                                   # install/sync dependencies from uv.lock
uv run python manage.py runserver         # dev server
uv run python manage.py migrate           # apply migrations
uv run python manage.py makemigrations    # generate migrations after model changes
uv run pytest --cov                       # full test suite with coverage
uv run pytest tests/test_smoke.py::test_smoke   # single test
uv run ruff check .                       # lint
uv run ruff format --check .              # formatting check (drop --check to apply)
```

## Architecture notes

- **`config/`** is the Django project package (`settings.py`, `urls.py`, `asgi.py`, `wsgi.py`). `DJANGO_SETTINGS_MODULE` is `config.settings`. `settings.py` is still the `startproject` default — `SECRET_KEY` is hardcoded, `DEBUG=True`, SQLite (`db.sqlite3`), and `INSTALLED_APPS` contains only Django built-ins.
- **`tests/`** is a top-level directory (not per-app). `pytest-django` is configured via `DJANGO_SETTINGS_MODULE = "config.settings"` in `[tool.pytest.ini_options]`. Tests that touch the database must be marked with the `@pytest.mark.django_db` decorator.
- **`main.py`** is a leftover `uv init` stub (`print("Hello...")`), unrelated to the Django app.

## Conventions

- Ruff: line length 88, target py314, rules `E`/`F`/`I` (includes import sorting). `config/settings.py` is exempt from `E501`.
- `db.sqlite3`, `.coverage`, and `.venv` are gitignored; `uv.lock` is committed for reproducible installs.
