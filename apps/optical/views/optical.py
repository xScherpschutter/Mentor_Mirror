from django.views.generic import View
from django.views import View
from django.http import JsonResponse, Http404
from django.shortcuts import render
import json
from apps.optical.components.get_glasses import get_glasses
from apps.optical.models import UserGlasses, Glasses
from django.shortcuts import get_object_or_404

class OpticalModulesView(View):
    template_name = 'optical_modules.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context = {})

class OpticalView(View):
    template_name = 'optical.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context = {
            "module_name": "Recomendación óptica"
        })
        
class OpticalGlasses(View):
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            face_shape = data['face_shape']
            
            
            query_set, condition = get_glasses(face_shape.lower())
            
            if condition: 
                glasses_list  = [glass.to_dict() for glass in query_set]
                glasses = {'success': True, 'data': glasses_list}
                
                return JsonResponse(glasses)
        
            return JsonResponse (
                {'success': False, 'data': None}
            )
        
        except Exception as e:
            print(e)
            return JsonResponse (
                {'success': False, 'data': None}
            )
            
class SaveGlasses(View):
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            token = data.get('token', None)
            
            user = request.user
            
            if token is None: return JsonResponse ({'success': False}, status=400)
            
            glass = get_object_or_404(Glasses, token = token)
            
            user_glass = UserGlasses.objects.create( user = user, glass = glass)
            
            return JsonResponse ({'success': True})
            
        except Http404 as e:
            print('404: ', e)
            return JsonResponse ({'success': False}, status=404)
        
        except Exception as e:
            print('Excepción:', e)
            return JsonResponse ({'success': False}, status=400)