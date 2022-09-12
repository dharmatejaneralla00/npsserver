from django.db import models


# Create your models here.

class Patentapplication(models.Model):
    uid = models.CharField(max_length=20)
    title = models.CharField(max_length=1000)
    organisation = models.CharField(max_length=100)
    modeofcontact = models.CharField(max_length=50)
    referedby = models.CharField(max_length=100)
    conntactnumber = models.CharField(max_length=10)
    emailid = models.EmailField(max_length=50)
    patenttype = models.CharField(max_length=30)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.uid


class ApplicationStatus(models.Model):
    status = models.BooleanField(default=False)
    uid = models.CharField(max_length=20)
    paymentstatus = models.BooleanField(default=False)