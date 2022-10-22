from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from tatbikat.mesanid.models import Fihrist, Hesab
from tatbikat.mustecirin.models import Hatm, Mustecir
from .managers import MustahdimManager, MuvazzafManager



class Mesuliyet(Hatm):
    mustecir = models.ForeignKey(Mustecir, on_delete=models.CASCADE, blank=True, null=True)
    yol = models.CharField(max_length=255, blank=True, null=True)
    isim = models.CharField(max_length=255, verbose_name=_("İsim"), blank=True, null=True)
    fihrist = models.ForeignKey(Fihrist, on_delete=models.CASCADE, blank=True, null=True)


class Salahiyet(Hatm):
    mustecir = models.ForeignKey(Mustecir, on_delete=models.CASCADE, blank=True, null=True)
    yol = models.CharField(max_length=255, blank=True, null=True)
    isim = models.CharField(max_length=255, verbose_name=_("İsim"), blank=True, null=True)
    fihrist = models.ForeignKey(Fihrist, on_delete=models.CASCADE, blank=True, null=True)
    mesuliyet = models.ForeignKey(Mesuliyet, on_delete=models.CASCADE, blank=True, null=True)


class Vazife(Hatm):
    mustecir = models.ForeignKey(Mustecir, on_delete=models.CASCADE, blank=True, null=True)
    yol = models.CharField(max_length=255, blank=True, null=True)
    isim = models.CharField(max_length=255, verbose_name=_("İsim"), blank=True, null=True)
    fihrist = models.ForeignKey(Fihrist, on_delete=models.CASCADE, blank=True, null=True)
    salahiyet = models.OneToOneField(Salahiyet, on_delete=models.CASCADE, blank=True, null=True)



class Muvazzaf(Hesab):

    objects = MuvazzafManager()
    
    class Meta:
        proxy = True
        ordering = ('isim',)


class Mustahdim(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    mumtaz = models.BooleanField(default=False)
    ad = models.CharField(max_length=124, blank=True, null=True)
    soyad = models.CharField(max_length=124, blank=True, null=True)

    mustecir = models.ForeignKey(Mustecir, on_delete=models.CASCADE, blank=True, null=True)
    mesuliyetler = models.ManyToManyField(Mesuliyet, blank=True)
    muvazzaf = models.ForeignKey(Muvazzaf, on_delete=models.CASCADE, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MustahdimManager()

    def __str__(self):
        return self.email


class Tarihce(models.Model):
    email = models.EmailField(unique=True, null=True, blank=True)
    mustahdim = models.ForeignKey(Mustahdim, on_delete=models.CASCADE)
    current_os = models.CharField(max_length=124, blank=True, null=True)
    current_os_version = models.CharField(max_length=124, blank=True, null=True)
    current_browser = models.CharField(max_length=124, blank=True, null=True)
    current_browser_version = models.CharField(max_length=124, blank=True, null=True)
    logged_in_at = models.DateTimeField(auto_now_add=True)
    otp = models.CharField(max_length=6, blank=True, null=True)

