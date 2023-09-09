from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    user_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='profile_pics'+'/'+str(datetime.datetime.now()), default='default.jpg')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.user_name
