from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, id, first_name, last_name, role, password):
        if not id:
            raise ValueError('The User must have an ID')
        
        user = self.model(
            id=id,
            first_name=first_name,
            last_name=last_name,
            role=role,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, first_name, last_name, role, password):
        user = self.create_user(
            id=id,
            first_name=first_name,
            last_name=last_name,
            role=role,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('leader', 'Leader'),
        ('manager', 'Manager'),
        ('administrator', 'Administrator'),
    )

    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'id'
    objects = CustomUserManager()

    def __str__(self):
        return str(self.id)
