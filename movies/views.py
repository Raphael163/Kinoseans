from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie

from .forms import ReviewForm


class MoviesView(ListView):
    """Вывод фильмов список главная """
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/index_list.html"


class MovieDetailView(DetailView):
    """Детальная страничка фильма"""
    model = Movie
    slug_field = 'url'


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


