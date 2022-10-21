import uuid
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class Hatm(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    kayit_tarihi = models.DateTimeField(auto_now_add=True)
    tadilat_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tatbik(Hatm):

    isim = models.CharField(max_length=255)
    meshur_isim = models.CharField(max_length=255, blank=True, null=True)
    sebike = models.SlugField(unique=True, blank=True, null=True)
    teallukat = models.CharField(max_length=255, blank=True, null=True)
    miftah = models.IntegerField()
    faaldir = models.BooleanField(default=False)
    fiyat = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name=_("Fiyat"),
        help_text=_("max 9999999,99"),
        default=10,
    )

    class Meta:
        ordering = ["miftah"]
        verbose_name_plural = _("Uygulama")
        verbose_name_plural = _("Uygulamalar")
    
    def __str__(self) -> str:
        return self.isim



class Mustecir(Hatm):
    unvan = models.CharField(_("Unvan"), max_length=250)
    ad = models.CharField(_("Ad"), max_length=124, null=True, blank=True)
    soyad = models.CharField(_("Soyad"), max_length=124, null=True, blank=True)
    telefon = PhoneNumberField(
        verbose_name=_("telefon"), max_length=30, default="+901234567899"
    )
    tatbikat = models.ManyToManyField(Tatbik, blank=True)
    adres = models.TextField(blank=True, null=True)
    vergi_dairesi = models.CharField(max_length=124, blank=True, null=True)
    vergi_numarasi = models.CharField(max_length=124, blank=True, null=True)
    il = models.CharField(max_length=124, blank=True, null=True)
    ilce = models.CharField(max_length=124, blank=True, null=True)
    ulke = CountryField(multiple=False, blank=True, null=True)
    sebike = models.SlugField(blank=True, null=True)
    eposta = models.EmailField(_('Eposta Adresi'), blank=True, null=True)
    mumtaz = models.BooleanField(default=False)
    resim_url = models.ImageField(
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("Resim URL'si"),
        upload_to="images/",
        default="images/default.png",
        help_text=_("format: zorunlu, default-default.png"),
    )

    def __str__(self) -> str:
        return self.unvan


