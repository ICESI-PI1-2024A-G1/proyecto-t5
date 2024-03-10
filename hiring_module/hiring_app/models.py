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

class ApplicationTemplate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# TODO: Add fields for the ApplicationTemplate model

class ApplicationTemplateManager(models.Manager):
    def create_application_template(self, id, name, created_by):
        if not id:
            raise ValueError('The Application Template must have an ID')
        
        if not created_by:
            raise ValueError('The Application Template must have a creator')
        
        application_template = self.model(
            id=id,
            name=name,
            created_by=created_by,
        )

        application_template.save(using=self._db)
        return application_template