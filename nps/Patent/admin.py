from django.contrib import admin
from .models import Patentapplication, ApplicationStatus

# Register your models here.

admin.site.register(Patentapplication)
admin.site.register(ApplicationStatus)
