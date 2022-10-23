from django.urls import path

from .views import (
    mustahdimin, yeni_mustahdim, tatbikati_mustahdim, tatbik_i_mustahdim
)

app_name = "uygulamalar"

urlpatterns = [
    path('users/', mustahdimin, name='mustahdimin'),
    path('users/new/', yeni_mustahdim, name='yeni_mustahdim'),
    path('users/<pk>/', tatbikati_mustahdim, name='tatbikati_mustahdim'),
    path('user-application/<pk>/<sebike>/', tatbik_i_mustahdim, name='tatbik_i_mustahdim'),
]
