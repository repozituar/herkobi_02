from django.contrib import admin
from .models import Mustahdim, Salahiyet, Mesuliyet, Vazife

admin.site.register(Mustahdim)
admin.site.register(Mesuliyet)
admin.site.register(Salahiyet)
admin.site.register(Vazife)