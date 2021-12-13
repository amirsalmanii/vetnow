from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    avatar = models.ImageField(upload_to='users/%Y/%m/', null=True, blank=True)
    national_code = models.CharField(max_length=10, null=True, blank=True)
    job = models.CharField(max_length=150, null=True, blank=True)
    graduate = models.CharField(max_length=150, null=True, blank=True)
    experience = models.CharField(max_length=20, null=True, blank=True)
    doctorDescreption = models.TextField(null=True, blank=True)
    doctorId = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = MyUserManager()

    is_doctor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_lable):
        return True

    @property
    def is_staff(self):
        return self.is_admin