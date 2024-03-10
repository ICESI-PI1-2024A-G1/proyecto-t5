from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from hiring_module.settings import MEDIA_ROOT
import os

class CustomUserManager(BaseUserManager):
    def create_user(self, id, first_name, last_name, birth_date, gender, address, role, password):
        if not id:
            raise ValueError('Users must have an ID')

        user = self.model(
            id=id,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            gender=gender,
            address=address,
            role=role,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, first_name, last_name, birth_date, gender, address, role, password):
        user = self.create_user(
            id=id,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            gender=gender,
            address=address,
            role=role,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('leader', 'Leader'),
        ('manager', 'Manager'),
        ('administrator', 'Administrator'),
        ('solicitant', 'Solicitant'),
        ('normal', 'Normal')
    )

    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
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
    
class ContractRequestManager(models.Manager):
    def create_contract_request(self, created_by, template, user_information=None, estimated_completion_date=None):
        if not created_by:
            raise ValueError('The Contract Request must have a creator')
        if not template:
            raise ValueError('The Contract Request must have a template')
        contract_request = self.model(
            created_by=created_by,
            template=template,
            current_state_start=timezone.now(),
            estimated_completion_date=estimated_completion_date,
            user_information=user_information
        )
        contract_request.save(using=self._db)
        return contract_request

    
class ContractRequestState(models.Model):
    contract_request = models.ForeignKey('ContractRequest', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ContractRequest(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    estimated_completion_date = models.DateTimeField()
    current_state_start = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    template = models.ForeignKey(ApplicationTemplate, on_delete=models.CASCADE)
    state = models.ForeignKey(ContractRequestState, on_delete=models.PROTECT)
    user_information = models.FileField(upload_to=os.path.join(MEDIA_ROOT, 'user_information'), null=True, blank=True)
    def __str__(self):
        return str(self.id)

    def transition_to_state(self, new_state, comment=None):
        previous_state = self.state

        self.state = new_state
        self.current_state_start = timezone.now()
        self.save()

        ContractRequestSnapshot.objects.create(
            contract_request=self,
            state=str(previous_state),
            state_start=self.current_state_start,
            state_end=timezone.now(),
            comment=comment
        )

        return previous_state 
    
    def get_snapshots(self):
        return ContractRequestSnapshot.objects.filter(contract_request=self)

class ContractRequestSnapshot(models.Model):
    contract_request = models.ForeignKey(ContractRequest, on_delete=models.CASCADE)
    state = models.CharField(max_length=64)
    state_start = models.DateTimeField()
    state_end = models.DateTimeField()
    comment = models.TextField()

    def __str__(self):
        return str(self.id)

class ContractRequestReviewState(ContractRequestState):
    def __str__(self):
        return "Review"

class ContractRequestIncompleteState(ContractRequestState):
    def __str__(self):
        return "Incomplete"

class ContractRequestFiledState(ContractRequestState):
    def __str__(self):
        return "Filed"
    
class ContractRequestCancelledState(ContractRequestState):
    def __str__(self):
        return "Cancelled"