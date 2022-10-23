from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _

from tatbikat.mustecirin.models import Hatm, Mustecir
from tatbikat.mesanid.models import Hesab
from .utils import belge_no_yap

class Sened(Hatm):
    
    mustecir = models.ForeignKey(Mustecir, on_delete=models.CASCADE, blank=True, null=True)
    
    hesabini_muktariz = models.BooleanField(default=True)
    
    hesab = models.ForeignKey(Hesab, related_name='hesab', on_delete=models.CASCADE, blank=True, null=True)
    mahsub = models.ForeignKey(Hesab, related_name='mahsub', on_delete=models.CASCADE, blank=True, null=True)

    mustened = models.BooleanField(default=False)
    izafe_edildi = models.BooleanField(default=False)

    belge_no = models.CharField(max_length=36, blank=True, null=True)
    belge_tarihi = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.belge_no = belge_no_yap()
        super(Sened, self).save(*args, **kwargs)


class Kalem(Hatm):
    mustecir = models.ForeignKey(Mustecir, on_delete=models.CASCADE, blank=True, null=True)
    
    hesab = models.ForeignKey(Hesab, related_name='kalem_hesabi', on_delete=models.CASCADE, blank=True, null=True)
    mahsub = models.ForeignKey(Hesab, related_name='kalem_mahsubu', on_delete=models.CASCADE, blank=True, null=True)
    
    mustened = models.BooleanField(default=False)
    izafe_edildi = models.BooleanField(default=False)
    
    aded = models.IntegerField()
    birim = models.CharField(max_length=124, blank=True, null=True)
    fiyat = models.DecimalField(
        verbose_name=_("Fiyat"),
        help_text=_("MEn fazla 99999.99"),
        error_messages={
            "name": {
                "max_length": _("En fazla 99999.99."),
            },
        },
        max_digits=7,
        decimal_places=2,
    )


class Mazmun(Hatm):
    mustecir = models.ForeignKey(Mustecir, on_delete=models.CASCADE, blank=True, null=True)
    
    hesab = models.ForeignKey(Hesab, related_name='mazmun_hesabi', on_delete=models.CASCADE, blank=True, null=True)
    mahsub = models.ForeignKey(Hesab, related_name='mazmun_mahsubu', on_delete=models.CASCADE, blank=True, null=True)
    
    mustened = models.BooleanField(default=False)
    izafe_edildi = models.BooleanField(default=False)
    
    meblag = models.DecimalField(
        verbose_name=_("Meblağ"),
        help_text=_("MEn fazla 9999999.99"),
        error_messages={
            "name": {
                "max_length": _("En fazla 9999999.99."),
            },
        },
        max_digits=9,
        decimal_places=2,
    )
