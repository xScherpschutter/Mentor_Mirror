from django.urls import path
from apps.haircut.views import haircut

app_name = "Haircut Module"
urlpatterns = [
    path('', haircut.HaircutView.as_view(), name="index"),
]