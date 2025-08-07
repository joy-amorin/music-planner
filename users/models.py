from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class CustomUser(AbstractBaseUser):

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

