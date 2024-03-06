from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from bigcorp.settings import MEDIA_ROOT

# app_name = 'shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include(('shop.urls', 'shop'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
