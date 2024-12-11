from enum import unique
from django.db import models
from django import forms


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    profile_picture = models.ImageField(upload_to='profilepictures/', blank=True)
    bio = models.TextField(max_length=200, blank=True)
    followers = models.ManyToManyField('self', related_name='followers')
    following = models.ManyToManyField('self', related_name='following')
    #implement skills later(13/10/24)
    github_url = models.URLField(max_length=200, blank=True)
    linkedin_url = models.URLField(max_length=200, blank=True)
    objects = models.Manager()

    def __str__(self):
        usnme = str(self.username)
        pwd = str(self.password)
        id = str(self.id)
        return f'{self.id} {self.username} {self.email} {self.password}'
    def to_dict(self):
        model_dict = {
            "id":self.id,
            "username":self.username,
            "email":self.email,
            "linkedin":self.linkedin_url,
            "github":self.github_url,
            "followers":self.followers.count(),
            "following":self.following.count(),
            "bio":self.bio

        }
        return model_dict



class editform(forms.ModelForm):
    class Meta:
        model = User
        fields = ["profile_picture", "username", "bio", "github_url", "linkedin_url",]
