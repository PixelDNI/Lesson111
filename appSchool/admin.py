from django.contrib import admin
from .models import Instruments
# Register your models here.
from .models import Student

admin.site.register(Student)
admin.site.register(Instruments)