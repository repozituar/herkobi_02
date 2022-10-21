from django.urls import path

from .views import (
    custom_login, otp, profile
)

app_name= 'mustahdimin'

urlpatterns = [
    path('login/', custom_login, name='login'),
    path('verification/', otp, name='otp'),
    path('profile/', profile, name='profile'),
]