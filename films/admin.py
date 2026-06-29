# Register your models here.
from django.contrib import admin

from .models import Favorite, Movie, Review

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Favorite)