from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    desciption = models.TextField()
    price = models.IntegerField()
    genre = models.TextField(null=True)
    author = models.CharField(max_length=100)
    year = models.DateField()
    is_favorites = models.BooleanField(default=False)
   