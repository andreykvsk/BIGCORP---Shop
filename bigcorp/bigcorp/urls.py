from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django_email_verification import urls as email_urls
from bigcorp.settings import MEDIA_ROOT


urlpatterns = [
    path('',  RedirectView.as_view(url='shop')),
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('account/', include('account.urls', namespace='account')),
    path('email/', include(email_urls), name='email-verification')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
