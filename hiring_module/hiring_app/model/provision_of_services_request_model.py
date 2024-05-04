from django.db import models
from .contract_request_model import ContractRequest
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Description: Manager class for ProvisionOfServicesContractRequest instances.
# Input: None
# Output: None
class ProvisionOfServicesContractRequestManager(models.Manager):

    # Description: Creates a new ProvisionOfServicesContractRequest instance.
    # Input: Keyword arguments for additional fields.
    # Output: New ProvisionOfServicesContractRequest instance.
    def create_contract_request(self, **extra_fields):
        self.model = ProvisionOfServicesContractRequest
        from .course_schedule_model import CourseSchedule
        course_schedules = extra_fields.pop('course_schedules')
        provision_of_services_request = self.create(
            **extra_fields
        )
        provision_of_services_request.create_snapshot()
        provision_of_services_request.save(using=self._db)
        for course_schedule_ in course_schedules:
            course_schedule = CourseSchedule.objects.create_schedule(
                pos_contract_request=provision_of_services_request,
                date=course_schedule_['date'],
                start_time=course_schedule_['start_time'],
                end_time=course_schedule_['end_time'],
                room=course_schedule_['room'],
                responsability=course_schedule_['responsability']
            )
            course_schedule.save()
        return provision_of_services_request

# Description: Model class for provision of services contract requests.
# Input: None
# Output: None
class ProvisionOfServicesContractRequest(ContractRequest):
    objects = ProvisionOfServicesContractRequestManager()

    BANK_ACCOUNT_CHOICES = [
        ('checking', 'Checking'),
        ('savings', 'Savings')
    ]
    hiree_full_name = models.CharField(max_length=256)
    hiree_id = models.IntegerField()
    hiree_cellphone = models.CharField(max_length=16)
    hiree_email = models.EmailField()
    cenco = models.CharField(max_length=128)
    request_motive = models.TextField()
    banking_entity = models.CharField(max_length=128)
    bank_account_type = models.CharField(max_length=64, choices=BANK_ACCOUNT_CHOICES)
    bank_account_number = models.CharField(max_length=32)
    eps = models.CharField(max_length=64)
    pension_fund = models.CharField(max_length=64)
    arl = models.CharField(max_length=64, null=True)
    contract_value = models.DecimalField(max_digits=16, decimal_places=2)
    charge_account = models.TextField(null=True)
    rut = models.FileField(upload_to='rut/', max_length=500)    
    course_name = models.CharField(max_length=256)
    period = models.CharField(max_length=64)
    group = models.CharField(max_length=2)
    intensity = models.IntegerField()
    total_hours = models.IntegerField()
    course_code = models.CharField(max_length=16)
    students_quantity = models.IntegerField()
    additional_hours = models.IntegerField()

    # Description: Clean method to validate model fields.
    # Input: None
    # Output: None
    def clean(self):
        super().clean()
        try:
            validate_email(self.hiree_email)
        except ValidationError:
            raise ValidationError({'email': 'Invalid email format'})

        if self.bank_account_type not in dict(self.BANK_ACCOUNT_CHOICES).keys():
            raise ValidationError({'bank_account_type': 'Invalid bank account type'})

    # Description: Save method to ensure validation before saving.
    # Input: None
    # Output: None
    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)

    # Description: String representation of the ProvisionOfServicesContractRequest instance.
    # Input: None
    # Output: String representation of the instance.
    def __str__(self):
        return str(self.id)
