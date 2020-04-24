from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path

from rest.views import ShowHelloWorld


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
