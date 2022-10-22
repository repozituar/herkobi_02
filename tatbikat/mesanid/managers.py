from django.db import models



class StokManager(models.Manager):
    def get_queryset(self):
        return super(StokManager, self).get_queryset().filter(kufl__in=[153, ])

