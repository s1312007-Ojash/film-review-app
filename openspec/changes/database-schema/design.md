## Context

The project is a fresh Django 6 / Python 3.14 skeleton: `config/` holds the project, the only apps are Django built-ins, and the dev database is SQLite. This change introduces the first domain models (`Movie`, `Review`, `Favorite`) and nothing else — no views, forms, templates, or admin. It depends only on `django.contrib.auth` (the built-in `User`), already in `INSTALLED_APPS`.

## Goals / Non-Goals

**Goals:**
- A single Django app holding all three models with their relationships and constraints.
- Average rating computed from reviews (never stored), as specified.
- Database-level uniqueness for one-review-per-user-per-movie and one-favorite-per-user-per-movie.
- `__str__` on every model for readable admin/shell display.

**Non-Goals:**
- No views, forms, templates, serializers, admin registration, or URL wiring.
- No custom user model — use `django.contrib.auth.models.User`.
- No image upload handling — the poster is a path/URL string.
- No denormalized/cached rating column.

## Decisions

- **One app named `films`.** All three models live together; they share the `Movie` foreign key and will be served by the same future views. Alternative considered: separate `reviews`/`favorites` apps — rejected as over-structuring for three tightly-coupled models in a small project. (Matches `AGENTS.md`: a feature means a new app added to `INSTALLED_APPS`.)
- **Reference `User` via `settings.AUTH_USER_MODEL`, not a direct import.** Even though we use the built-in `User`, referencing `settings.AUTH_USER_MODEL` in the FK is the idiomatic, swap-safe pattern. Alternative: `from django.contrib.auth.models import User` — works but is more brittle if the user model is ever swapped.
- **Poster as `URLField`-or-`CharField` path/URL string.** Avoids `ImageField` (which pulls in Pillow and media handling) since the spec says path/URL. Using a plain field keeps the dependency surface at zero.
- **Average rating computed via aggregation, defined as a model method/property** (e.g. `Avg('reviews__rating')`) rather than a stored field — single source of truth, always consistent. No signals or save-time recomputation needed.
- **Rating bounds enforced with validators** (`MinValueValidator(0)`, `MaxValueValidator(5)`) on a `PositiveSmallIntegerField`/`IntegerField`. Validators cover form/serializer validation; a `CheckConstraint` may additionally enforce it at the DB level for defense in depth.
- **Uniqueness via `Meta.constraints = [UniqueConstraint(fields=["user", "movie"], ...)]`** (the modern replacement for `unique_together`) on both `Review` and `Favorite`. Behaviorally identical to the `unique_together` the request named, but the current idiom in Django 6.
- **Timestamps:** `Review.created` = `auto_now_add=True`, `Review.updated` = `auto_now=True`; `Favorite.date_added` = `auto_now_add=True`.
- **`related_name`s** set on FKs (`movie.reviews`, `movie.favorites`, `user.reviews`, `user.favorites`) so the computed-average aggregation and future queries read naturally.

## Risks / Trade-offs

- **Risk: computed average runs a query per call / N+1 in future list views** → Mitigation: out of scope now; future views will use `annotate(Avg(...))`. The model property is correct-by-default; performance tuning belongs with the views that consume it.
- **Risk: `UniqueConstraint` vs the literally-requested `unique_together`** → Mitigation: they are equivalent in effect; `UniqueConstraint` is the non-deprecated form in Django 6. Behavior the spec requires (reject duplicates) is preserved.
- **Trade-off: no `ImageField`** means no validation that the poster path points at a real image — accepted, since the spec calls for a path/URL and we avoid the Pillow dependency.

## Migration Plan

Create the `films` app, add it to `INSTALLED_APPS`, run `uv run python manage.py makemigrations films` then `uv run python manage.py migrate`. Greenfield tables, so rollback is dropping the new migration (and tables) — no data migration concerns. Verify with `uv run python manage.py makemigrations --check` (no pending changes) and the existing `uv run pytest`.
