from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, username, **extra_fields):
        if not username:
            raise ValueError('User must be have username')
        user = self.model(username=username, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.model(username=username, password=password, **extra_fields)
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user
