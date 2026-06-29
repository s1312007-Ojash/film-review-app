# Film Catalog Specification

## Purpose

Defines the `Movie` entity — the catalog of films that can be browsed and reviewed. A movie's average rating is a computed value derived from its reviews, never a stored field.

## Requirements

### Requirement: Movie entity

The system SHALL provide a `Movie` model representing a film in the catalog, with a `title`, a `description`, and a poster reference stored as a path or URL string.

#### Scenario: Create a movie

- **WHEN** a `Movie` is created with a title, description, and poster path/URL
- **THEN** the record is persisted and retrievable from the database

#### Scenario: Poster stored as a reference, not a binary

- **WHEN** a `Movie`'s poster is set
- **THEN** it is stored as a path or URL string (not an uploaded binary blob)

### Requirement: Average rating is computed, not stored

The `Movie` model SHALL NOT persist an average-rating field; the average rating is derived from the movie's related reviews at read time.

#### Scenario: No stored average field

- **WHEN** the `Movie` schema is inspected
- **THEN** there is no database column holding a precomputed average rating

#### Scenario: Average reflects current reviews

- **WHEN** a review's rating changes or a review is added or removed for a movie
- **THEN** any computed average derived from that movie's reviews reflects the change without a separate update step

### Requirement: Readable string representation

The `Movie` model SHALL define a `__str__` method returning a human-readable label (the title) for admin and shell display.

#### Scenario: Admin display

- **WHEN** a `Movie` instance is rendered as a string
- **THEN** it returns the movie's title rather than a default object identifier
