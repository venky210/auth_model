from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    

    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['username','first_name','last_name']


    