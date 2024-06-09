from django.urls import path
from apps.optical.views import optical

app_name = "Optical Module"
urlpatterns = [
    path('', optical.OpticalModulesView.as_view(), name="index" ),
    path('features/', optical.OpticalView.as_view(), name="optical_features" ),
    path('glass/', optical.OpticalGlasses.as_view(), name="glass"),
    path('save_glass/', optical.SaveGlasses.as_view(), name="save_glass")
]