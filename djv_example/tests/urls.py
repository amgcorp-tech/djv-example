"""URLs to run the tests."""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.views.i18n import JavaScriptCatalog

last_modified_date = timezone.now()
admin.autodiscover()

urlpatterns = [
    path('jsi18n/',
         cache_page(86400, key_prefix='js18n-%s' % last_modified_date)(
             JavaScriptCatalog.as_view(
                 packages=[
                     'djv_example'
                 ]
             )
         ),
         name='javascript-catalog'
    ),
    path('admin/', admin.site.urls),

]

# App Api urls here...
urlpatterns += [

]


urlpatterns += i18n_patterns(

    # Include app urls here...
    path('', include('djv_example.urls')),
)