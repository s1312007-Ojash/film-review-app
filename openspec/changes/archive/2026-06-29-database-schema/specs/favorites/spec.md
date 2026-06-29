## ADDED Requirements

### Requirement: Favorite entity

The system SHALL provide a `Favorite` model that links a Django built-in `User` to a `Movie` and records the date the favorite was added.

#### Scenario: Add a favorite

- **WHEN** an authenticated user marks a movie as a favorite
- **THEN** a `Favorite` record is persisted linking that user and movie, with the date-added timestamp set

### Requirement: One favorite per user per movie

The system SHALL enforce that a given user has at most one favorite entry for a given movie, via a uniqueness constraint on the (user, movie) pair.

#### Scenario: Duplicate favorite rejected

- **WHEN** a user who has already favorited a movie attempts to favorite the same movie again
- **THEN** the database uniqueness constraint rejects the duplicate

### Requirement: Readable string representation

The `Favorite` model SHALL define a `__str__` method returning a human-readable label identifying the user and movie for admin and shell display.

#### Scenario: Admin display

- **WHEN** a `Favorite` instance is rendered as a string
- **THEN** it returns a label referencing the user and the favorited movie
