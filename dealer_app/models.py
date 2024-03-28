from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,Permission,Group

class Dealer(AbstractUser):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=100)
    

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions'  # Change the related_name to a unique value
    )
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups'  # Change the related_name to a unique value
    )
    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['username']


   