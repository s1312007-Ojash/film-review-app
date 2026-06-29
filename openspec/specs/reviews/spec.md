# Reviews Specification

## Purpose

Defines the `Review` entity linking a user to a movie with review text, a 0–5 star rating, and timestamps. A user may review a given movie at most once.

## Requirements

### Requirement: Review entity

The system SHALL provide a `Review` model that links a Django built-in `User` to a `Movie` and stores review `text`, an integer star `rating`, and `created` and `updated` timestamps.

#### Scenario: Create a review

- **WHEN** an authenticated user submits a review for a movie with text and a rating
- **THEN** a `Review` record is persisted linking that user and movie, with `created` and `updated` timestamps set

#### Scenario: Timestamps maintained

- **WHEN** a `Review` is first saved
- **THEN** `created` is set once at creation and `updated` is refreshed on every subsequent save

### Requirement: Star rating bounded 0 to 5

The `Review` `rating` SHALL be an integer constrained to the inclusive range 0 to 5.

#### Scenario: Valid rating accepted

- **WHEN** a review is saved with a rating between 0 and 5 inclusive
- **THEN** the review is accepted

#### Scenario: Out-of-range rating rejected

- **WHEN** a review is validated with a rating below 0 or above 5
- **THEN** validation fails and the review is not considered valid

### Requirement: One review per user per movie

The system SHALL enforce that a given user has at most one review for a given movie, via a uniqueness constraint on the (user, movie) pair.

#### Scenario: Duplicate review rejected

- **WHEN** a user who already has a review for a movie attempts to create a second review for the same movie
- **THEN** the database uniqueness constraint rejects the duplicate

### Requirement: Readable string representation

The `Review` model SHALL define a `__str__` method returning a human-readable label identifying the user and movie for admin and shell display.

#### Scenario: Admin display

- **WHEN** a `Review` instance is rendered as a string
- **THEN** it returns a label referencing the reviewing user and the movie
