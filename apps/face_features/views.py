from django.views.generic import View
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
import json
import base64
import os
import tempfile
from apps.face_features.face_features import optical_face_features

class FaceFeaturesView(View):
    def post(self, request, *args, **kwargs):
        try:
            
            body = request.body.decode('utf-8')
            body_data = json.loads(body)
            image_data_base64 = body_data['image']
            image_data_binary = base64.b64decode(image_data_base64.split(',')[1])

            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            temp_file.write(image_data_binary)
            temp_file.close()
            image_path = temp_file.name

            face_type, success, img_base64 = optical_face_features(image_path)
            os.unlink(temp_file.name)
            
            if success:
                return JsonResponse({'success': True, 'message': face_type, 'image': img_base64})
            
            else:
                return JsonResponse({'success': False, 'message': face_type, 'image': img_base64 if img_base64 else None })
        
        except Exception as e:
            print('Error: {}'.format(e))
            return JsonResponse({'success': False, 'message': str(e), 'image': None})