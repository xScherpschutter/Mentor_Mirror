from django.views.generic import TemplateView
from apps.core.mixins import UserGroupMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeTemplateView(UserGroupMixin, LoginRequiredMixin, TemplateView):
    template_name = 'index/home.html'

