import pytest
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction

from films.models import Favorite, Movie, Review


@pytest.fixture
def user(db):
    return User.objects.create_user(username="alice", password="pw")


@pytest.fixture
def other_user(db):
    return User.objects.create_user(username="bob", password="pw")


@pytest.fixture
def movie(db):
    return Movie.objects.create(title="Inception", description="A heist in dreams.")


@pytest.mark.django_db
def test_movie_str(movie):
    assert str(movie) == "Inception"


@pytest.mark.django_db
def test_review_str(user, movie):
    review = Review.objects.create(user=user, movie=movie, text="Great", rating=4)
    assert str(review) == "alice on Inception: 4/5"


@pytest.mark.django_db
def test_favorite_str(user, movie):
    favorite = Favorite.objects.create(user=user, movie=movie)
    assert str(favorite) == "alice ♥ Inception"


@pytest.mark.django_db
def test_average_rating_with_multiple_reviews(user, other_user, movie):
    Review.objects.create(user=user, movie=movie, rating=2)
    Review.objects.create(user=other_user, movie=movie, rating=5)
    assert movie.average_rating == pytest.approx(3.5)


@pytest.mark.django_db
def test_average_rating_with_no_reviews(movie):
    assert movie.average_rating is None


@pytest.mark.django_db
def test_one_review_per_user_per_movie(user, movie):
    Review.objects.create(user=user, movie=movie, text="First", rating=3)
    with pytest.raises(IntegrityError):
        with transaction.atomic():
            Review.objects.create(user=user, movie=movie, text="Duplicate", rating=1)


@pytest.mark.django_db
def test_one_favorite_per_user_per_movie(user, movie):
    Favorite.objects.create(user=user, movie=movie)
    with pytest.raises(IntegrityError):
        with transaction.atomic():
            Favorite.objects.create(user=user, movie=movie)
