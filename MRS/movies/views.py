from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Movie

# Create your views here.
@login_required(login_url='login')
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)

def details(request, id):
    movie = Movie.objects.get(id=id)
    context = {'movie': movie}
    return render(request, 'movies/details.html', context)