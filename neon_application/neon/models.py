from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    password  = models.CharField(max_length=32)



class skills(models.Model):
    skill = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
class hobbies(models.Model):
    hobby = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
class projects(models.Model):
    project = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    
    
    
    

