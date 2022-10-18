from django.db import models


# Create your models here.
class Pertsona(models.Model):
    dni = models.CharField(max_length=9)
    izena = models.CharField(max_length=255)
    abizena = models.CharField(max_length=255)
    jaiotzeData = models.CharField(max_length=10)

    def __str__(self):
        return u'%s' % self.dni

class Kotxea(models.Model):
    matrikula=models.CharField(max_length=7)
    marka=models.CharField(max_length=255)
    modeloa=models.CharField(max_length=255)
    urtea=models.CharField(max_length=4)

    def __str__(self):
        return u'%s' % self.matrikula

class KotxeaPertsona(models.Model):
    dniPertsona = models.ForeignKey(Pertsona, on_delete=models.CASCADE)
    matrikula=models.ForeignKey(Kotxea, on_delete=models.CASCADE)
    alokairuData=models.CharField(max_length=10)

    def __str__(self):
        return u'%s' % self.dniPertsona+"-en alokairua"
