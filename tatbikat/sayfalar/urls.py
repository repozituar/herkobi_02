from django.urls import path

from .views import anasayfa

app_name = "sayfalar"

urlpatterns = [
    path('', anasayfa, name="anasayfa")
]
