from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page, never_cache
from django.views.generic.list import ListView
from . models import Album
from django.utils.decorators import method_decorator
from django.core.cache import cache


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# @method_decorator(cache_page(CACHE_TTL, key_prefix='album-list'), name='dispatch')
# @method_decorator(never_cache, name='dispatch')
# @method_decorator(cache_page(CACHE_TTL), name='dispatch')
class AlbumListView(ListView):
    model = Album


    def get_template_names(self):
        return 'core/album-list.html'


def album_list(request):
    print('Uncached')
    result = cache.get('result', default=None)
    object_list = Album.objects.all()
    if result is None:
        result = (29 * 49 / 98 + 309999 - 3)
        print('Cached successfully')
        cache.set('result', result, 20)
    return render(request, 'core/album-list.html', {'result': result, 'object_list': object_list})

