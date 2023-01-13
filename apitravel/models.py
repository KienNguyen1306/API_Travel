from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m',default=False)



class Travels(models.Model):
    image = models.TextField(null=True,blank=True)
    name = models.TextField(null=True,blank=True)
    sub = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name


class TestimonialsData(models.Model):
    image = models.TextField(null=True,blank=True)
    job = models.TextField(null=True,blank=True)
    name = models.TextField(null=True,blank=True)
    sub = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name


class FrequentlyAskedDatas(models.Model):
    title = models.TextField(null=True,blank=True)
    answer = models.TextField(null=True,blank=True)
    open = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class PostDatas(models.Model):
    image = models.TextField(null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    name = models.TextField(null=True,blank=True)
    sub = models.TextField(null=True,blank=True)



    def __str__(self):
        return self.name
    

class Teamsdata(models.Model):
    image = models.TextField(null=True,blank=True)
    job = models.TextField(null=True,blank=True)
    name = models.TextField(null=True,blank=True)
    sub = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.name



class FeaturedServicwesDatas(models.Model):
    image = models.TextField(null=True,blank=True)
    name = models.TextField(null=True,blank=True)
    sub = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
