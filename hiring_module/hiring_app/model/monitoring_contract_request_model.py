from django.db import models
from django.core.exceptions import ValidationError
from .user_model import CustomUser
from .contract_request_model import ContractRequest
from django.core.validators import validate_email

# Description: Manager class for MonitoringContractRequest instances.
# Input: None
# Output: None
class MonitoringContractRequestManager(models.Manager):

    # Description: Creates a new MonitoringContractRequest instance.
    # Input: Keyword arguments for additional fields.
    # Output: New MonitoringContractRequest instance.
    def create_contract_request(self, **extra_fields):
        self.model = MonitoringContractRequest
        monitoring_contract_request = self.create(
            **extra_fields
        )
        monitoring_contract_request.create_snapshot()
        monitoring_contract_request.save(using=self._db)
        return monitoring_contract_request

# Description: Model class for monitoring contract requests.
# Input: None
# Output: None
class MonitoringContractRequest(ContractRequest):
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

    # Description: Clean method to validate model fields.
    # Input: None
    # Output: None
    def clean(self):
        super().clean()
        try:
            validate_email(self.student_email)
        except ValidationError:
            raise ValidationError({'email': 'Invalid email format'})

    # Description: Save method to ensure validation before saving.
    # Input: None
    # Output: None
    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)

    # Description: String representation of the MonitoringContractRequest instance.
    # Input: None
    # Output: String representation of the instance.
    def __str__(self):
        return str(self.id)
