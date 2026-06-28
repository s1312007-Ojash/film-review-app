# Film Review Web Application

## Overview

The Film Review Web Application is a Django-based web application where users can browse movies, read reviews, and check average star ratings. Registered users can write and update their own reviews, give movies a rating from 0 to 5, and save favorite movies to view later from their profile page.

## Tech Stack

* Python 3.14
* Django 6.0

## Development Environment

This project uses `uv` to manage the virtual environment and project dependencies. Using `uv` makes the development environment easier to reproduce, installs dependencies quickly, and allows the lockfile to be committed for consistent setup across different machines.

Git is used for version control, and `uv.lock` is committed so that dependencies can be reproduced consistently.

## Tools

* `ruff` — used for formatting and linting Python code.
* `pytest` with `pytest-django` — used for running the test suite.
* `pytest-cov` — used for measuring test coverage.

## Setup

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd <repository-name>
```

Install dependencies:

```bash
uv sync
```

Apply database migrations:

```bash
uv run python manage.py migrate
```

Run the development server:

```bash
uv run python manage.py runserver
```

Then open the local development URL in your browser.

## Running Checks

Run the test suite with coverage:

```bash
uv run pytest --cov
```

Run the linter:

```bash
uv run ruff check .
```
Check formatting:

```bash
uv run ruff format --check .
```

## Project Structure

The `config/` directory contains the main Django project settings and configuration files. The `manage.py` file is the main entry point for Django management commands. The `tests/` directory contains the test suite for checking the behavior of the application.