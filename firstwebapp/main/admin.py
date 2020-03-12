from django.contrib import admin
from .models import Artist, Album, Track, Photo, Video

# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Photo)
admin.site.register(Video)
