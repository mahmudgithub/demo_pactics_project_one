#from django.db import models

# Create your models here.

from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    roll = models.IntegerField()
    #class Meta:
    #  verbose_name_plural = "cities"

    def __str__(self):
        return self.name
