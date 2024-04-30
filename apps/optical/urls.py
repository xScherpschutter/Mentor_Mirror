from django.urls import path
from apps.optical.views import optical

app_name = "Optical Module"
urlpatterns = [
    path('', optical.OpticalView.as_view(), name="index" ),
]