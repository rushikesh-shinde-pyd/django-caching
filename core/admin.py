from django.contrib import admin
from . models import Album


class AlbumAdmin(admin.ModelAdmin):
    fields = ('name', 'artist')


admin.site.register(Album, AlbumAdmin)