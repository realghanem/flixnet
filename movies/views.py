from django.shortcuts import render
from .models import Movie
# Create your views here.


def home(request):
    movies = Movie.objects.all()
    context_dict = {'movies': movies}
    return render(request, "movies/home.html", context_dict)
