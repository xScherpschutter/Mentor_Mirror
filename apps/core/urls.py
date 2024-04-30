from django.urls import path
from apps.core.views import home, modules, about, profile, logs

app_name = 'core'
urlpatterns = [
    path('', home.HomeTemplateView.as_view(), name ="home"),
    path('modules/', modules.ModulesTemplateView.as_view(), name="modules"),
    path('about/', about.AboutTemplateView.as_view(), name="about"),
    path('profile/', profile.ProfileTemplateView.as_view(), name= "profile"),
    path('login/', logs.LoginView.as_view(), name= "login"),
    path('register/', logs.RegisterView.as_view(), name= "register"),
    path('logout/', logs.LogoutView.as_view(), name= "logout"),
    path('withoutpermissions/', logs.NoPermissions.as_view(), name= "withoutpermissions"),
]
