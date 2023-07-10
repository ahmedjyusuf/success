from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import pytz

TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    timezone = models.CharField(max_length=50, choices=TIMEZONE_CHOICES, null=True, blank=True)
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.first_name
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils import timezone

# import pytz

# class User(AbstractUser): 
#     username = models.CharField(max_length=150, unique=False, default='')
#     email = models.EmailField(unique=True)
#     TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]
#     timezone = models.CharField(max_length=50, choices=TIMEZONE_CHOICES, null=True, blank=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
