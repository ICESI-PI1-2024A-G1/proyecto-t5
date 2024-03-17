from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

class CustomUserManager(BaseUserManager):
    def create_user(self, id, password, **extra_fields):
        # Create and save a User with the given id and extra fields.
        if not id:
            raise ValueError('Users must have an ID')

        user = self.model(
            id=id,
            **extra_fields
        )
    
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, id, password, **extra_fields):
        # Create and save a SuperUser with the given id and extra fields.
        user = self.create_user(
            id=id,
            password=password,
            **extra_fields
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Custom user model
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, help_text='The groups this user belongs to.', related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', related_name='customuser_set')
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'id' 
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birth_date', 'gender', 'address']
    objects = CustomUserManager()

    def __str__(self):
        return str(self.id)