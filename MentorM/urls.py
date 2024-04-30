
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls', namespace="core")),
    path('management/', include('apps.security.urls', namespace="security")),
    path('optical/', include('apps.optical.urls', namespace="optical")),
    path('haircut/', include('apps.haircut.urls', namespace='haircut'))
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)