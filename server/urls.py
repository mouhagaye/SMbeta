from django.urls import include, path

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path('main/', include('main.urls')),
    path('auth/', include('authentification.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

