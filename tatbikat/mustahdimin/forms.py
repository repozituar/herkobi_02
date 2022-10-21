from django import forms
from allauth.account.forms import SignupForm

from .models import Tarihce

class CustomSignupForm(SignupForm):
    def custom_signup(self, request, user):
        Tarihce.objects.create(
            email=user.email,
            mustahdim=user,
            current_os=request.user_agent.os.family,
            current_os_version=request.user_agent.os.version,
            current_browser=request.user_agent.browser.family,
            current_browser_version=request.user_agent.browser.version,
        )
        user.mumtaz = True
        user.save()

class TarihceForm(forms.ModelForm):
    class Meta:
        model=Tarihce
        fields=['otp']


