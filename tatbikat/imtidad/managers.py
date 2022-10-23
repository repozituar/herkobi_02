from django.db import models

class KasaManager(models.Manager):
    def get_queryset(self):
        return super(KasaManager, self).get_queryset().filter(kufl=100)


class BankaManager(models.Manager):
    def get_queryset(self):
        return super(BankaManager, self).get_queryset().filter(kufl=102)


class CekManager(models.Manager):
    def get_queryset(self):
        return super(CekManager, self).get_queryset().filter(kufl=101)


class MusteriManager(models.Manager):
    def get_queryset(self):
        return super(MusteriManager, self).get_queryset().filter(kufl=120)

class TicariMalManager(models.Manager):
    def get_queryset(self):
        return super(TicariMalManager, self).get_queryset().filter(kufl=120)

class PersonelManager(models.Manager):
    def get_queryset(self):
        return super(PersonelManager, self).get_queryset().filter(kufl=135)

class SaticiManager(models.Manager):
    def get_queryset(self):
        return super(SaticiManager, self).get_queryset().filter(kufl=120)


class YurticiSatisManager(models.Manager):
    def get_queryset(self):
        return super(YurticiSatisManager, self).get_queryset().filter(kufl=600)


class IhracatManager(models.Manager):
    def get_queryset(self):
        return super(IhracatManager, self).get_queryset().filter(kufl=601)


class IadeManager(models.Manager):
    def get_queryset(self):
        return super(IadeManager, self).get_queryset().filter(kufl=610)


class IskontoManager(models.Manager):
    def get_queryset(self):
        return super(IskontoManager, self).get_queryset().filter(kufl=611)


class StmmManager(models.Manager):
    def get_queryset(self):
        return super(StmmManager, self).get_queryset().filter(kufl=621)

class ShmManager(models.Manager):
    def get_queryset(self):
        return super(ShmManager, self).get_queryset().filter(kufl=622)


class ArgeGiderleriManager(models.Manager):
    def get_queryset(self):
        return super(ArgeGiderleriManager, self).get_queryset().filter(kufl=630)

class PazarlamaGiderleriManager(models.Manager):
    def get_queryset(self):
        return super(PazarlamaGiderleriManager, self).get_queryset().filter(kufl=631)


class YonetimgiderleriManager(models.Manager):
    def get_queryset(self):
        return super(YonetimgiderleriManager, self).get_queryset().filter(kufl=632)

class HerkobiManager(models.Manager):
    def get_queryset(self):
        return super(HerkobiManager, self).get_queryset().filter(kufl=323)


class AbonelikManager(models.Manager):
    def get_queryset(self):
        return super(AbonelikManager, self).get_queryset().filter(kufl=323)

