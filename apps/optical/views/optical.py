from django.views.generic import View
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
import json

class OpticalView(View):
    template_name = 'optical.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context = {
            "module_name": "Recomendación óptica"
        })
        
