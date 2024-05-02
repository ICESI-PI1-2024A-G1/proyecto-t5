from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .user_model import CustomUser
from .contract_request_model import ContractRequest
from hiring_module.settings import MEDIA_ROOT
import os

# Description: Manager class for CEX contract requests.
# Input: None
# Output: None
class CEXContractRequestManager(models.Manager):

    # Description: Creates a new CEX contract request instance.
    # Input: Keyword arguments for additional fields.
    # Output: New CEX contract request instance.
    def create_contract_request(self, **extra_fields):
        # Create a CEX contract request
        cex_contract_request = self.create(
            **extra_fields
        )
        cex_contract_request.create_snapshot()
        cex_contract_request.save(using=self._db)
        return cex_contract_request

# Description: Model class for CEX contract requests, inheriting from ContractRequest.
# Input: None
# Output: None
class CEXContractRequest(ContractRequest):
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

    objects = CEXContractRequestManager()
    
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

    # Description: String representation of the CEX contract request instance.
    # Input: None
    # Output: String representation of the instance.
    def __str__(self):
        return str(self.id)
