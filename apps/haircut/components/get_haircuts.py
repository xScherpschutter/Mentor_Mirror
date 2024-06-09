from apps.haircut.models import Haircuts

def get_haircuts (shape : str, race: str, gender: str):
    try:
         haircuts = Haircuts.objects.filter(face_shape = shape, race = race, gender = gender)
         
         if not haircuts: return None, False
         
         return haircuts, True
         
    except Exception as e:
        return e, False