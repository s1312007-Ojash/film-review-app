## 1. Create and register the app

- [x] 1.1 Create the `films` Django app (`uv run python manage.py startapp films`).
- [x] 1.2 Add `"films"` to `INSTALLED_APPS` in `config/settings.py`.

## 2. Define models

- [x] 2.1 In `films/models.py`, add the `Movie` model: `title`, `description`, poster path/URL field (no stored average rating), and a `__str__` returning the title.
- [x] 2.2 Add a computed average-rating method/property on `Movie` that aggregates related reviews' ratings (no stored field).
- [x] 2.3 Add the `Review` model: FK to `settings.AUTH_USER_MODEL` and FK to `Movie` (with `related_name`s), `text`, integer `rating` with `MinValueValidator(0)`/`MaxValueValidator(5)`, `created` (`auto_now_add`), `updated` (`auto_now`), a unique constraint on (user, movie), and a `__str__`.
- [x] 2.4 Add the `Favorite` model: FK to `settings.AUTH_USER_MODEL` and FK to `Movie` (with `related_name`s), date-added timestamp (`auto_now_add`), a unique constraint on (user, movie), and a `__str__`.

## 3. Migrations

- [x] 3.1 Generate the initial migration (`uv run python manage.py makemigrations films`).
- [x] 3.2 Apply migrations (`uv run python manage.py migrate`).

## 4. Tests

- [x] 4.1 Add a test module for the models in `films/tests/` (e.g. `films/tests/test_models.py`, with `films/tests/__init__.py`), using pytest and `@pytest.mark.django_db` on DB-touching tests.
- [x] 4.2 Test each model's `__str__` returns the expected readable label (Movie title; Review and Favorite referencing user + movie).
- [x] 4.3 Test the computed average rating: a movie with multiple reviews returns the correct average, and a movie with no reviews returns a sensible empty value (e.g. `None`/`0`).
- [x] 4.4 Test the one-review-per-user-per-movie constraint: creating a second `Review` for the same (user, movie) raises `IntegrityError` (wrap in `transaction.atomic` so the test DB stays usable).
- [x] 4.5 Test the one-favorite-per-user-per-movie constraint: creating a second `Favorite` for the same (user, movie) raises `IntegrityError`.

## 5. Verify

- [x] 5.1 Confirm no pending model changes (`uv run python manage.py makemigrations --check --dry-run`).
- [x] 5.2 Run `uv run python manage.py check` and `uv run pytest` to confirm the project loads and all tests pass.
- [x] 5.3 Run `uv run ruff check .` and `uv run ruff format --check .` on the new code.
