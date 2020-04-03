
# Create your views here.
from .models import Movie
from django.shortcuts import render, redirect


def get_movie_list(request):
    if request.method == 'GET':
        
        movielist = Movie.objects.all().order_by('-popularity')[:5]
        print(movielist)
        return render(request, 'movie/home.html',
                      {'movie_list': movielist})
