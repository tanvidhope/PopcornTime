
# Create your views here.
from movie.models import Movie
from django.shortcuts import render, redirect


def get_movie_list(request):
    if request.method == 'GET':
        movielist = Movie.objects.all().order_by('popularity')[:10]
        return render(request, 'home.html',
                      {'movie_list': movielist})
