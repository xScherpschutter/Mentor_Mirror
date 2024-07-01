
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from apps.core.views.errors import error_404

handler404 = error_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls', namespace="core")),
    path('management/', include('apps.security.urls', namespace="security")),
    path('optical/', include('apps.optical.urls', namespace="optical")),
    path('haircut/', include('apps.haircut.urls', namespace='haircut')),
    path('face_features/', include('apps.face_features.urls', namespace = 'face_features'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)