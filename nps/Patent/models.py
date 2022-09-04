from django.db import models

# Create your models here.
class FullPatentapplication(models.Model):
    title = models.CharField(max_length=20)
    organisation = models.CharField(max_length=30)
    resource = models.IntegerField()
    modeofcontact = models.EmailField(max_length=50)
    referedby = models.IntegerField()
    conntactnumber = models.CharField(max_length=10)
    emailid = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

class Patentapplication(models.Model):
    title = models.CharField(max_length=20)
    organisation = models.CharField(max_length=30)
    resource = models.IntegerField()
    modeofcontact = models.EmailField(max_length=50)
    referedby = models.IntegerField()
    conntactnumber = models.CharField(max_length=10)
    emailid = models.EmailField(max_length=50)
    patenttype=models.CharField(max_length=30)

    def __str__(self):
        return self.name