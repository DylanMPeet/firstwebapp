from django.shortcuts import render
from .models import Album, Track, Photo, Video

# Create your views here.
# Views - different web pages


def index(response, id):
    project = Album.objects.get(id=id)
    return render(response, "main/albums.html", {"project": project})


def home(response):
    return render(response, "main/home.html", {})


def album(response, id):
    project = Album.objects.get(id=id)
    return render(response, 'main/albums.html', {"project": project})


def photo(request):
    img = Photo.objects.all()
    return render(request, 'main/photo.html', {"img": img})


def video(request):
    vid = Video.objects.all()
    return render(request, 'main/video.html', {"vid": vid})


def view(request):
    a = Album.objects.all()
    return render(request, "main/view.html", {"albums": a})

