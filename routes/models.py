from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True, unique = True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    
    objects = models.Manager()

    def __str__(self):
        usnme = str(self.username)
        pwd = str(self.password)
        id = str(self.id)
        return id + ':'+usnme +" : "+pwd


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200)
    followers = models.ManyToManyField('self', related_name='followers')
    following = models.ManyToManyField('self', related_name='following')
    #implement skills later(13/10/24)
    github_url = models.URLField(max_length=200, unique=True)
    linkedin_url = models.URLField(max_length=200, unique=True)


