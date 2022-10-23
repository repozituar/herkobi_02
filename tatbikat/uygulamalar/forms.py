from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from tatbikat.mustahdimin.models import Mustahdim

class MuvazzafSinupForm(UserCreationForm):

    ad = forms.CharField(required=True)
    soyad = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = Mustahdim
        fields = ('email',)
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.ad = self.cleaned_data.get('ad')
        user.soyad = self.cleaned_data.get('soyad')
        user.save()
        return user