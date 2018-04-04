from django.conf.urls import url, include
from django.contrib import admin

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login_redirect),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^music/', include('music.urls', namespace='music')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
