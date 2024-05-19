from django.db import models


# Create your models here.
class Clas(models.Model):

    objects = None
    fname = models.CharField(max_length=255)
    lname  = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"#{self.id} {self.fname} {self.lname} who is {self.age} "