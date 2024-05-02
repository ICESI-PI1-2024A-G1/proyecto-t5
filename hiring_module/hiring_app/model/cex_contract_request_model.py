# Import necessary modules from Django
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Import local modules
from .user_model import CustomUser
from .contract_request_model import ContractRequest
from hiring_module.settings import MEDIA_ROOT
import os

# Define a manager for CEXContractRequest objects
class CEXContractRequestManager(models.Manager):
    def create_contract_request(self, **extra_fields):
        # Create a CEX contract request
        cex_contract_request = self.create(
            **extra_fields
        )
        # Create a snapshot of the contract request
        cex_contract_request.create_snapshot()
        # Save the contract request to the database
        cex_contract_request.save(using=self._db)
        return cex_contract_request
    
# Define the CEXContractRequest model, which inherits from ContractRequest
class CEXContractRequest(ContractRequest):
    # Define choices for bank account type
    BANK_ACCOUNT_CHOICES = [
        ('checking', 'Checking'),
        ('savings', 'Savings')
    ]
    # Define fields for the CEXContractRequest model
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

    # Assign the custom manager to the objects attribute
    objects = CEXContractRequestManager()
    
    def clean(self):
        # Call the clean method of the superclass
        super().clean()
        # Validate the email field
        try:
            validate_email(self.hiree_email)
        except ValidationError:
            # Raise a validation error if the email is invalid
            raise ValidationError({'email': 'Invalid email format'})

        # Validate the bank account type
        if self.bank_account_type not in dict(self.BANK_ACCOUNT_CHOICES).keys():
            # Raise a validation error if the bank account type is invalid
            raise ValidationError({'bank_account_type': 'Invalid bank account type'})

    def save(self, *args, **kwargs):
        # Ensure validation is triggered before saving
        self.full_clean()  
        super().save(*args, **kwargs)

    def __str__(self):
        # Return the string representation of the object
        return str(self.id)
