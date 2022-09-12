from django.contrib import admin
from .models import  ApplicationStatus

from .models import Patentapplication
# Register your models here.

admin.site.register(Patentapplication)
admin.site.register(ApplicationStatus)