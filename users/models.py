from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model.
    Defines methods for creating regular users and superusers.
    """
    def create_user(self, email, password=None):
        """
        Create and save a user with email and encrypted password.
        """
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)  # Normalize the email (convert the domain to lowercase)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and save a superuser with administrator permissions.
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that uses email as a unique identifier.
    """
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
