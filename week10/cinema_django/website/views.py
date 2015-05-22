from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Movie, Projection, Reservation


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'base.html', locals())
