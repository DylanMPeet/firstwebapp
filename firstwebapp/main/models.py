from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    release_date = models.DateTimeField(null=True, blank=True)
    artwork = models.ImageField(upload_to="static/", default='', blank=True, null=True)

    def __str__(self):
        return self.title


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    song = models.FileField(upload_to="static/", default='', blank=True, null=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="static/", default='', blank=True, null=True)

    def __str__(self):
        return str(self.image)


class Video(models.Model):
    videos = models.FileField(upload_to="static/", default='', blank=True, null=True)

    def __str__(self):
        return str(self.videos)

