from django.views.generic import TemplateView
from apps.core.mixins import UserGroupMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class AboutTemplateView(UserGroupMixin, LoginRequiredMixin, TemplateView):
    template_name = 'index/about.html'