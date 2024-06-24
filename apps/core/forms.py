from .models import Costumer
from django import forms

class CostumerForm(forms.ModelForm):
    class Meta:
        model = Costumer
        fields = ['first_name', 'last_name', 'id_number', 'email' ,'phone_number', 'address']
        
    first_name = forms.CharField(label='Nombres del Cliente')
    last_name = forms.CharField(label='Apellidos del Cliente')
    id_number = forms.CharField(label='Cedula del Cliente')
    email = forms.EmailField(label='Correo Electrónico')
    phone_number = forms.CharField(label='Teléfono', widget=forms.TextInput(attrs={'type': 'tel'}))
    address = forms.CharField(label='Dirección')