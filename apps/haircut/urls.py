from django.urls import path
from apps.haircut.views import haircut, haircut_list

app_name = "Haircut Module"
urlpatterns = [
    
    path('', haircut.HaircutModulesView.as_view(), name="index"),
    path('features/', haircut.HaircutView.as_view(), name="haircut_features"),
    path('haircuts/', haircut.Haircuts.as_view(), name="haircuts"),
    path('haircut_list/', haircut_list.HaircutList.as_view(), name="haircut_list"),
    path('save_haircut/', haircut.SaveHaircuts.as_view(), name="save_haircut"),
    
]