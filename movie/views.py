
# Create your views here.
from .models import Movie
from django.shortcuts import render, redirect
import requests
from .forms import NameForm


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
        return render(request, 'movie/recommendation.html',
                      {'movie_list': response.json()})

def genre_based(request):
    if request.method == 'GET':
        response = requests.post('http://127.0.0.1:5000/genre', json={"title": "The Dark Knight Rises"})
        print(response.json()) # This should contain the returned data
        return render(request, 'movie/genre.html',
            {'movie_list': response.json()})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            title = form.cleaned_data['title']
            response = requests.post('http://127.0.0.1:5000/genre', json={"title": title})
            print(response.json()) # This should contain the returned data
            return render(request, 'movie/genre.html',
                {'movie_list': response.json()})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'movie/form.html', {'form': form})