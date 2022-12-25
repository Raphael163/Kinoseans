"""импорт из models"""
from django.contrib import admin
from .models import Category
from .models import Actor
from .models import Genre
from .models import Movie
from .models import MovieShots
from .models import RatingStar
from .models import Rating
from .models import Reviews

""" Регистрируем модельки """
admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
