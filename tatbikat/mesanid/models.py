from django.db import models
from django.utils.translation import gettext_lazy as _

from tatbikat.mustecirin.models import Hatm, Mustecir
from .managers import StokManager

class Fihrist(Hatm):
    mustecir = models.ForeignKey(Mustecir, on_delete=models.CASCADE)
    isim = models.CharField(max_length=255, verbose_name=_("Uygulama İsimi"))
    sebike = models.SlugField(unique=True, blank=True, null=True)
    kufl = models.IntegerField(unique=True)
    faaldir = models.BooleanField(default=False)
    borc = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name=_("Borç"),
        help_text=_("max 9999999,99"),
        default=0,
    )
    alacak = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name=_("Alacak"),
        help_text=_("max 9999999,99"),
        default=0,
    )

    class Meta:
        verbose_name = _('Etkin Uygulama')
        verbose_name_plural = _('Etkin Uygulamalar')

    def __str__(self) -> str:
        return self.isim


class Hesab(Hatm):
    mustecir = models.ForeignKey(Mustecir, on_delete=models.CASCADE, blank=True, null=True)
    fihrist = models.ForeignKey(Fihrist, on_delete=models.CASCADE, blank=True, null=True)
    isim = models.CharField(max_length=255, verbose_name=_("İsim"))
    kufl = models.IntegerField()
    borc = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name=_("Borç"),
        help_text=_("max 9999999,99"),
        default=0,
    )
    alacak = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name=_("Alacak"),
        help_text=_("max 9999999,99"),
        default=0,
    )

    def __str__(self) -> str:
        return self.isim

def stok_fihristi_getir(miftah):
    fihrist_qs = Fihrist.objects.filter(kufl=miftah)
    if fihrist_qs.exists:
        return fihrist_qs.first()
    return None


class Stok(Hesab):
    
    giren = models.IntegerField(default=0)
    cikan = models.IntegerField(default=0)
    faaldir = models.BooleanField(default=False)
    kdv_orani = models.IntegerField(default=8)

    stoklar = StokManager()

    def __str__(self) -> str:
        return self.isim
    
    def save(self, *args, **kwargs):
        self.kufl = 153
        self.fihrist = stok_fihristi_getir(153)
        super(Stok, self).save(*args, **kwargs)


class Depo(Hatm):
    
    isim = models.CharField(max_length=255, verbose_name=_("İsim"))
    stok = models.ForeignKey(Stok, on_delete=models.CASCADE)
    giren = models.IntegerField(default=0)
    cikan = models.IntegerField(default=0)
    faaldir = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.isim


