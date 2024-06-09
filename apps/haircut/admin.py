from django.contrib import admin
from apps.haircut.models import Haircuts, UserHaircuts

admin.site.register(Haircuts)
admin.site.register(UserHaircuts)