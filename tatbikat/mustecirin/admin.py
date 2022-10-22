from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Tatbik, Mustecir

# Register your models here.
class TatbikResource(resources.ModelResource):
    class Meta:
        model=Tatbik

class TatbikAdmin(ImportExportModelAdmin):
    resource_class = TatbikResource

admin.site.register(Tatbik, TatbikAdmin)
admin.site.register(Mustecir)