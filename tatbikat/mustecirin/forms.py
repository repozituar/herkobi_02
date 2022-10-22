from django import forms

from .models import Mustecir

class MustecirForm(forms.ModelForm):
    class Meta:
        model=Mustecir
        fields = [
            'unvan', 'adres', 'vergi_dairesi', 'vergi_numarasi',
            'il', 'ilce'
        ]