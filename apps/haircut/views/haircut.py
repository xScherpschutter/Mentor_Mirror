from django.views.generic import View
from django.views import View
from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
import json
from django.shortcuts import get_object_or_404
from apps.haircut.models import UserHaircuts, Haircuts as HaircutsModel
from apps.haircut.components.get_haircuts import get_haircuts
from django.contrib.auth.mixins import LoginRequiredMixin

class HaircutModulesView(LoginRequiredMixin, View):
    template_name = 'haircut_modules.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context = {})

class HaircutView(LoginRequiredMixin, View):
    template_name = 'haircut.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context = {
            "module_name" : "Recomendación de peinados"
        })

class Haircuts(View):
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(data)
            face_shape = data['face_shape']
            race = data['race']
            gender = data['gender']
            
            query_set, condition = get_haircuts(face_shape.lower(), race, gender)
            
            if condition: 
                haircuts_list  = [haircut.to_dict() for haircut in query_set]
                haircuts = {'success': True, 'data': haircuts_list}
                
                return JsonResponse(haircuts)
        
            return JsonResponse (
                {'success': False, 'data': None}
            )
        
        except Exception as e:
            print(e)
            return JsonResponse (
                {'success': False, 'data': None}
            )
            
class SaveHaircuts(View):
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            token = data.get('token', None)
            user = request.user
            
            if token is None: return JsonResponse ({'success': False}, status=400)
            
            haircut = get_object_or_404(HaircutsModel, token = token)
            
            user_haircut = UserHaircuts.objects.create( user = user, haircut = haircut)
            
            return JsonResponse ({'success': True})
            
        except Http404 as e:
            print('404: ', e)
            return JsonResponse ({'success': False}, status=404)
        
        except Exception as e:
            print('Excepción:', e)
            return JsonResponse ({'success': False}, status=400)