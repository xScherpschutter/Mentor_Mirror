from django.urls import path
from apps.face_features.views import OpticalView, HaircutView

app_name = "Face Features"
urlpatterns = [
    path('optical/', OpticalView.as_view(), name="optical_recommendation"),
    path('haircut/', HaircutView.as_view(), name="haircut_recommendation"),
]