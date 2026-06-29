## Why

The app is still a skeleton with no domain models — `INSTALLED_APPS` holds only Django built-ins and there is nothing to browse, review, or favorite. The data model is the foundation every later feature (views, forms, templates, ratings) depends on, so it should be defined first and captured in the spec.

## What Changes

- Add a new Django app (e.g. `films`) to hold the domain models, wired into `INSTALLED_APPS`.
- Add a `Movie` model: `title`, `description`, and a poster stored as a path/URL string. **No** stored average rating — the average is derived from related reviews at read time, not persisted.
- Add a `Review` model linking Django's built-in `User` and a `Movie`, with review `text`, an integer star `rating` (0–5), and `created`/`updated` timestamps.
- Add a `Favorite` model linking `User` and `Movie` with a `date added` timestamp.
- Enforce **one review per user per movie** and **one favorite per user per movie** via `unique_together` (user + movie) on each.
- Add `__str__` methods on all three models for readable Django admin display.
- Generate and commit the initial migration for the new app.
- Scope guard: schema only — **no views, forms, templates, admin registrations, or URL wiring** in this change.

## Capabilities

### New Capabilities
- `film-catalog`: The `Movie` entity — the catalog of films that can be browsed and reviewed, with the average rating defined as a computed (non-stored) value.
- `reviews`: The `Review` entity linking a user to a movie with text, a 0–5 star rating, and timestamps, constrained to one review per user per movie.
- `favorites`: The `Favorite` entity linking a user to a movie with a date-added timestamp, constrained to one favorite per user per movie.

### Modified Capabilities
<!-- None: no existing domain specs in openspec/specs/. -->

## Impact

- New code: a Django app package (models + migrations), and one line each in `config/settings.py` (`INSTALLED_APPS`) — no `config/urls.py` change since there are no views yet.
- Data: introduces the first three tables plus their unique constraints; uses the existing SQLite dev database.
- Dependencies: none added — uses Django built-ins (`django.contrib.auth.User`) only.
- No breaking changes (greenfield models).
