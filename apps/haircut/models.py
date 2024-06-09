from django.db import models
from apps.security.models import User
from MentorM.conts import FACE_SHAPE_CHOICES, RACE_CHOICES, GENDERS
import uuid

class Haircuts(models.Model):
    image = models.ImageField(verbose_name= 'Imagenes', name= 'Imagen', upload_to = 'haircuts/')
    name = models.CharField(verbose_name= 'Cortes', name = 'Corte', max_length= 30)
    face_shape = models.CharField(max_length= 20, choices= FACE_SHAPE_CHOICES)
    race = models.CharField(max_length= 20, choices= RACE_CHOICES, default= RACE_CHOICES[0][0])
    gender = models.CharField(max_length= 20, choices= GENDERS, default= GENDERS[0][0])
    token = models.UUIDField( default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.Corte
    
    def delete(self, *args, **kwargs):
        
        if self.Imagen:
            self.Imagen.delete(save=False)
            
        super(Haircuts, self).delete(*args, **kwargs)
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'image': self.Imagen.url if self.Imagen else None,
            'name': self.Corte,
            'token': self.token
        }
    
class UserHaircuts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    haircut = models.ForeignKey(Haircuts, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Fechas de realización', name = 'Fecha de realización', auto_now_add = True)
    
    def __str__(self):
        return f'{self.user.username} -  {self.haircut.Corte}'