
# Create your views here.
from .models import Movie
from django.shortcuts import render, redirect
import requests


def get_movie_list(request):
    if request.method == 'GET':
        response = requests.post('http://127.0.0.1:5000/popular')
        dictn = response.json()
        print(dictn)
        return render(request, 'movie/home.html',
                      {'movie_list': dictn})

def get_recomm(request):
    if request.method == 'GET':
        response = requests.post('http://127.0.0.1:5000/', json={"title": "The Dark Knight Rises"})
        print(response.json()) # This should contain the returned data
        # response.json = {'2329': 'Prom Night', '2298': 'Sex Drive', '4750': 'The Dirties', '3915': "Trippin'", '2392': 'Superbad', '2916': 'High School Musical 3: Senior Year', '3263': 'Easy A', '4024': 'The Spectacular Now', '2828': 'Project X', '3266': 'Prom'}
        return render(request, 'movie/recommendation.html',
                      {'movie_list': response.json()})
