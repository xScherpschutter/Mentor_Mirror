from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index/home.html'

