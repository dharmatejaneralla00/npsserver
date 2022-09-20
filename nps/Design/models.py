from django.db import models

# Create your models here.
class Design(models.Model):
    categoryofwork = models.CharField(max_length=20)
    clientname = models.CharField(max_length=30)
    titleofwork = models.IntegerField()
    modeofcontact = models.EmailField(max_length=50)
    referedby = models.IntegerField()
    conntactnumber = models.CharField(max_length=10)
    emailid = models.EmailField(max_length=50)
    uid = models.CharField(max_length=20)

    def __str__(self):
      return self.title


class Designstatus(models.Model):
    uid = models.CharField(max_length=20)
    quotationstatus = models.CharField(max_length=20)
    quotedamount = models.CharField(max_length=20)
    toassignteam = models.CharField(max_length=20)
    projectduedate = models.CharField(max_length=20)
    designcompleted = models.BooleanField(max_length=20)

    def __str__(self):
        return self.uid