from apps.optical.models import Glasses

def get_glasses (shape : str):
    try:
         glasses = Glasses.objects.filter(face_shape = shape)
         
         if not glasses: return None, False
         
         return glasses, True
         
    except Exception as e:
        return e, False