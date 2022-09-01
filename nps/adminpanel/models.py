from django.db import models

# Create your models here.


class PatentModel(models.Model):
    patenttype = models.CharField(max_length=30)

