from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Instruments(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name}'

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.CharField(max_length=50)
    instrument =  models.ManyToManyField(Instruments,null=True)


    performance =  models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    has_paid = models.BooleanField()


    def __str__(self):
        return f"{self.name} - {self.surname}"


    def get_absolute_url(self):
        return f"/students/{self.id}"



