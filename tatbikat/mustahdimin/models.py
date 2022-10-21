from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import MustahdimManager


class Mustahdim(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

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

