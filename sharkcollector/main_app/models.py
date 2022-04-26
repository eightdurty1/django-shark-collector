from django.db import models

# Create your models here.

class Shark(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()


#adding the __str__ method new code below
def __str__(self):
    return self.name



