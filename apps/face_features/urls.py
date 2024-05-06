from django.urls import path
from apps.face_features.views import FaceFeaturesView

app_name = "Face Features"
urlpatterns = [
    path('', FaceFeaturesView.as_view(), name="features" ),
]