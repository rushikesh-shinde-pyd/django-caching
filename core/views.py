from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page, never_cache
from django.views.generic.list import ListView
from . models import Album
from django.utils.decorators import method_decorator


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# @method_decorator(cache_page(CACHE_TTL, key_prefix='album-list'), name='dispatch')
# @method_decorator(never_cache, name='dispatch')
@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class AlbumListView(ListView):
    model = Album


    def get_template_names(self):
        return 'core/album-list.html'

