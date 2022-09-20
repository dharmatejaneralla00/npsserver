from django.db import models

# Create your models here.
class Design(models.Model):
    categoryofwork = models.CharField(max_length=100)
    clientname = models.CharField(max_length=100)
    titleofwork = models.CharField(max_length=1000)
    modeofcontact = models.EmailField(max_length=100)
    referedby = models.CharField(max_length=1000)
    conntactnumber = models.IntegerField(max_length=10)
    emailid = models.EmailField(max_length=100)
    uid = models.CharField(max_length=20)

    def __str__(self):
      return self.uid


class Designstatus(models.Model):
    uid = models.CharField(max_length=20)
    quotationstatus = models.CharField(max_length=20)
    quotedamount = models.CharField(max_length=20)
    toassignteam = models.CharField(max_length=20)
    projectduedate = models.CharField(max_length=20)
    designcompleted = models.BooleanField(max_length=20)

    def __str__(self):
        return self.uid