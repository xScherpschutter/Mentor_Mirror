from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.conf import settings

class User(AbstractUser):
  profile_picture = models.ImageField(("Imagen de perfil"), upload_to='profile_pics/', null=True, blank=True)
  groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='customuser_groups'
    )
  
  USERNAME_FIELD = "username"
  REQUIRED_FIELDS = ["first_name", "last_name"]
  
  class Meta:
    verbose_name = ("Usuario")
    verbose_name_plural = ("Usuarios")
  
  def __str__(self):
      return "{} - Email: {}".format(self.username, self.email)
  
  
  def save(self, *args, **kwargs):
    is_new_user = not self.pk
    super().save(*args, **kwargs)  
    
    if is_new_user:
        group, created = Group.objects.get_or_create(name='User')
        self.groups.add(group)
    
  def get_image_url(self):
    if self.profile_picture:
        return '{}{}'.format(settings.MEDIA_URL, self.profile_picture)
      
    else:
        return '/static/images/perfil.jpg'

