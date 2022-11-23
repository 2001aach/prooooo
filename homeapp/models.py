from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_user=models.BooleanField(default=False)
    is_worker=models.BooleanField(default=False)

class userpage(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='user')
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    housenumber=models.IntegerField(max_length=15)
    phonenumber=models.IntegerField(max_length=15)
    email=models.EmailField()
    photo=models.ImageField(upload_to='photo')


class workerpage(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='worker')
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    phonenumber = models.IntegerField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photo')
    workertype=models.CharField(max_length=100)









