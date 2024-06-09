from django.db import models
from apps.security.models import User
from MentorM.conts import FACE_SHAPE_CHOICES
import uuid

class Glasses(models.Model):
    image = models.ImageField(verbose_name= 'Imagenes', name= 'Imagen', upload_to = 'glasses/')
    name = models.CharField(verbose_name= 'Lentes', name = 'Lente', max_length= 30)
    face_shape = models.CharField(max_length= 20, choices= FACE_SHAPE_CHOICES)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    def __str__(self):
        return self.Lente
    
    def delete(self, *args, **kwargs):
        
        if self.Imagen:
            self.Imagen.delete(save=False)
            
        super(Glasses, self).delete(*args, **kwargs)
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'image': self.Imagen.url if self.Imagen else None,
            'name': self.Lente,
            'token': self.token
        }
    
class UserGlasses(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    glass = models.ForeignKey(Glasses, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Fechas de adquisición', name = 'Fecha de adquisición', auto_now_add = True)
    
    def __str__(self):
        return f'{self.user.username} -  {self.glass.Lente}'