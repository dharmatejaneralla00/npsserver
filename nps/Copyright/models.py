from django.db import models

# Create your models here.
class Copyright(models.Model):
    title = models.CharField(max_length=20)
    organisation = models.CharField(max_length=30)
    resource = models.IntegerField()
    modeofcontact = models.EmailField(max_length=50)
    referedby = models.IntegerField()
    conntactnumber = models.CharField(max_length=20)
    emailid = models.EmailField(max_length=20)
    uid=models.CharField(max_length=20)

    def __str__(self):
      return self.title


class Copyrightstatus(models.Model):
    uid = models.CharField(max_length=20)

    def __str__(self):
        return self.uid