from django.db import models

# Create your models here.
class Trademark(models.Model):
    title = models.CharField(max_length=20)
    organisation = models.CharField(max_length=30)
    resource = models.IntegerField()
    modeofcontact = models.EmailField(max_length=50)
    referedby = models.IntegerField()
    conntactnumber = models.CharField(max_length=10)
    emailid = models.EmailField(max_length=50)
    uid = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Trademarkstatus(models.Model):
    uid = models.CharField(max_length=20)
    quotationstatus = models.CharField(max_length=20)
    quotedamount = models.CharField(max_length=20)
    toassignteam = models.CharField(max_length=20)
    projectduedate = models.CharField(max_length=20)
    trademarkcompleted = models.BooleanField(max_length=20)

    def __str__(self):
        return self.uid