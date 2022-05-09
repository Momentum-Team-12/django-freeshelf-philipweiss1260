from nturl2path import url2pathname
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title       = models.CharField(max_length=255)
    author      = models.CharField(max_length=255)
    url         = models.URLField(blank=True,null=True)
    description = models.TextField(null=True, blank=True)
    date_added  = models.DateTimeField(auto_now_add=True)

class Description(models.Model):
    text = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey(Book, on_delete=models.CASCADE, related_name= "descriptions")