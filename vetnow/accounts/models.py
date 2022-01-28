from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.urls import reverse
from django.utils.html import format_html

from .managers import MyUserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    avatar = models.ImageField(upload_to='users/%Y/%m/', null=True, blank=True)
    national_code = models.CharField(max_length=10, null=True, blank=True)
    national_code_image = models.ImageField(upload_to='mojavezha/%Y/%m/', null=True, blank=True)
    job = models.CharField(max_length=150, null=True, blank=True)
    graduate = models.CharField(max_length=150, null=True, blank=True)
    experience = models.CharField(max_length=20, null=True, blank=True)
    doctorDescreption = models.TextField(null=True, blank=True)
    doctorId = models.CharField(max_length=100, null=True, blank=True)
    # mojavez ha
    Incubation_license = models.ImageField(upload_to='mojavezha/%Y/%m/', null=True, blank=True)
    other = models.ImageField(upload_to='mojavezha/%Y/%m/', null=True, blank=True)
    # for address
    state = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    plate = models.CharField(max_length=5, null=True, blank=True) # pelak khane
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = MyUserManager()

    is_employee = models.BooleanField(default=False)
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

    def get_absolute_url(self):
        return reverse('accounts:user_update', args=[self.id])

    def user_image(self):
        """
        for show avatar in admin panel
        """
        try:
            return format_html(f"<img src='{self.avatar.url}' width='80', height='70'>")
        except:
            return 'no image'


class IpTables(models.Model):
    ip = models.GenericIPAddressField()
    city = models.CharField(max_length=200)