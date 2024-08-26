from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=150, blank=True)
    objects = models.Manager()

    def __str__(self):
        usnme = str(self.username)
        pwd = str(self.password)
        return usnme +" : "+pwd