from turtle import title
from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=100,default='')
    author = models.CharField(max_length=100,default='')
    genre = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=100,default='')
    isbn = models.IntegerField()
    image = models.ImageField(upload_to ='media/')
    published = models.CharField(max_length=100,default='')
    publisher = models.CharField(max_length=100,default='')