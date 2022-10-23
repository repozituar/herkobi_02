from django import forms

from .models import Sened, Kalem, Mazmun

class IstirakForm(forms.ModelForm):
    class Meta:
        model = Sened
        fields = ['mustened']