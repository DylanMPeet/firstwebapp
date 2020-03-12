from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("albums/<int:id>", views.album, name="media"),
    path("photo/", views.photo, name="photo"),
    path("video/", views.video, name="video"),
    path("views/", views.view, name="view")
]