from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('tatbikat.mustahdimin.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('tatbikat.sayfalar.urls', namespace='sayfalar')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
