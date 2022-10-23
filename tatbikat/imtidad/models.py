from django.db import models
from .utils import (
    fihrist_getir
)
from .managers import (
    AbonelikManager,
    ArgeGiderleriManager,
    BankaManager,
    CekManager,
    HerkobiManager,
    IadeManager,
    IhracatManager,
    IskontoManager,
    KasaManager,
    MusteriManager,
    PazarlamaGiderleriManager,
    PersonelManager,
    SaticiManager,
    ShmManager,
    StmmManager,
    TicariMalManager,
    YonetimgiderleriManager,
    YurticiSatisManager,
)

from tatbikat.mesanid.models import (
    Hesab, Stok
)
from tatbikat.mustecirin.models import Mustecir



class Kasa(Hesab):

    objects = KasaManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(100)
        super(Stok, self).save(*args, **kwargs)


class Cek(Hesab):

    objects = CekManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(101)
        super(Stok, self).save(*args, **kwargs)


class Banka(Hesab):

    objects = BankaManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(102)
        super(Stok, self).save(*args, **kwargs)


class Musteri(Hesab):

    objects = MusteriManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(120)
        super(Stok, self).save(*args, **kwargs)


class Personel(Stok):

    objects = PersonelManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(135)
        super(Stok, self).save(*args, **kwargs)

class TicariMal(Stok):

    objects = TicariMalManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(153)
        super(Stok, self).save(*args, **kwargs)


class Satici(Stok):

    objects = SaticiManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(320)
        super(Stok, self).save(*args, **kwargs)


class YurticiSatis(Stok):

    objects = YurticiSatisManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(600)
        super(Stok, self).save(*args, **kwargs)


class Ihracat(Stok):

    objects = IhracatManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(601)
        super(Stok, self).save(*args, **kwargs)


class Iade(Stok):

    objects = IadeManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(610)
        super(Stok, self).save(*args, **kwargs)


class Iskonto(Stok):

    objects = IskontoManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(611)
        super(Stok, self).save(*args, **kwargs)


class Stmm(Stok):

    objects = StmmManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(621)
        super(Stok, self).save(*args, **kwargs)

class Shm(Stok):

    objects = ShmManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(622)
        super(Stok, self).save(*args, **kwargs)


class ArgeGiderleri(Stok):

    objects = ArgeGiderleriManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(630)
        super(Stok, self).save(*args, **kwargs)


class PazarlamaGiderleri(Stok):

    objects = PazarlamaGiderleriManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(631)
        super(Stok, self).save(*args, **kwargs)


class YonetimGiderleri(Stok):

    objects = YonetimgiderleriManager()

    class Meta:
        proxy = True
        ordering = ('isim', )
    
    def save(self, *args, **kwargs):
        self.kufl = 100
        self.fihrist = fihrist_getir(632)
        super(Stok, self).save(*args, **kwargs)


class Herkobi(Hesab):
    objects = HerkobiManager()
    class Meta:
        proxy = True
        ordering = ("isim", )


class Abonelik(Hesab):
    objects = AbonelikManager()
    class Meta:
        proxy = True
        ordering = ("isim", )
    
    def save(self, *args, **kwargs):
        self.kufl = 182
        self.fihrist = fihrist_getir(182)
        super(Abonelik, self).save(*args, **kwargs)

