from django.db import models
from django.core.exceptions import ValidationError
from .user_model import CustomUser
from .contract_request_model import ContractRequest
from django.core.validators import validate_email


class MonitoringContractRequestManager(models.Manager):
    def create_contract_request(self, **extra_fields):
        self.model = MonitoringContractRequest
        monitoring_contract_request = self.create(
            **extra_fields
        )
        monitoring_contract_request.save(using=self._db)
        return monitoring_contract_request
    
class MonitoringContractRequest(ContractRequest):
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='monitoring_contract_requests_assigned_to', null=True, blank=True)
    cenco = models.CharField(max_length=128)
    has_money_in_cenco = models.BooleanField()
    cenco_manager = models.CharField(max_length=256)
    monitoring_type = models.CharField(max_length=64, choices=[('academic', 'Academic'), ('office', 'Office')])
    student_code = models.CharField(max_length=16)
    student_full_name = models.CharField(max_length=256)
    student_id = models.CharField(max_length=16)
    student_email = models.EmailField()
    student_cellphone = models.CharField(max_length=16)
    daviplata = models.CharField(max_length=32)
    course_or_proyect = models.CharField(max_length=256)
    monitoring_description = models.TextField()
    weekly_hours = models.DecimalField(max_digits=4, decimal_places=2)
    total_value_to_pay = models.DecimalField(max_digits=16, decimal_places=2)
    is_unique_payment = models.BooleanField()

    objects = MonitoringContractRequestManager()

    def clean(self):
        super().clean()
        # Validate email field
        try:
            validate_email(self.student_email)
        except ValidationError:
            raise ValidationError({'email': 'Invalid email format'})
        
    def save(self, *args, **kwargs):
        # Ensure validation is triggered before saving
        self.full_clean()  
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
