from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg


class Movie(models.Model):
    """A film in the catalog. Average rating is computed from reviews, not stored."""

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # Poster stored as a path or URL string (not an uploaded binary).
    poster = models.CharField(max_length=500, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        """Mean of related reviews' star ratings, or None when there are no reviews."""
        return self.reviews.aggregate(average=Avg("rating"))["average"]


class Review(models.Model):
    """A user's review of a movie: text and a 0-5 star rating. One per user/movie."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    text = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "movie"],
                name="unique_review_per_user_per_movie",
            ),
            models.CheckConstraint(
                condition=models.Q(rating__gte=0) & models.Q(rating__lte=5),
                name="review_rating_between_0_and_5",
            ),
        ]

    def __str__(self):
        return f"{self.user} on {self.movie}: {self.rating}/5"


class Favorite(models.Model):
    """A user's favorited movie. One per user per movie."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites",
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="favorites",
    )
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "movie"],
                name="unique_favorite_per_user_per_movie",
            ),
        ]

    def __str__(self):
        return f"{self.user} ♥ {self.movie}"
