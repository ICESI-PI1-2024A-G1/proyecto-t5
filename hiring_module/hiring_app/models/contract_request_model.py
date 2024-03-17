from django.db import models
from .user_model import CustomUser
from django.utils import timezone
from hiring_module.settings import MEDIA_ROOT
import os
    
class ContractRequestManager(models.Manager):
    def create_contract_request(self, created_by, **extra_fields):
        # Create and save a Contract Request with the given creator and extra fields.
        if not created_by:
            raise ValueError('The Contract Request must have a creator')
        contract_request = self.model(
            created_by=created_by,
            current_state_start=timezone.now(),
            **extra_fields
        )
        contract_request.save(using=self._db)
        return contract_request


class ContractRequest(models.Model):
    # Contract Request model
    STATE_CHOICES = (
        ('pending', 'Pending'),
        ('review', 'Review'),
        ('incomplete', 'Incomplete'),
        ('filed', 'Filed'),
        ('cancelled', 'Cancelled')
    )
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    estimated_completion_date = models.DateTimeField(null = True)
    current_state_start = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    state = models.CharField(max_length=64, choices=STATE_CHOICES, default='pending')
    user_information = models.FileField(upload_to=os.path.join(MEDIA_ROOT, 'user_information'), null=True, blank=True)
    comment = models.TextField(null=True, default='')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_to', null=True, blank=True)

    REQUIRED_FIELDS = ['created_by']
    objects = ContractRequestManager()

    def __str__(self):
        return str(self.id) 
    
    def get_snapshots(self):
        # Get all snapshots of the contract request
        return ContractRequestSnapshot.objects.filter(contract_request=self)
    
    def edit_comment(self, comment):
        # Edit the comment of the contract request
        self.comment = comment
        self.save()
    
    def transition_to_state(self, new_state, comment=''):
        # Transition the contract request to a new state
        # If the new state is not valid, raise a ValueError
        if new_state not in dict(self.STATE_CHOICES).keys():
            raise ValueError('Invalid state provided')
        snapshots = self.get_snapshots()
        if (snapshots.filter(state=new_state).count() >= 1):
            # If the state transition has already been made, raise a ValueError
            raise ValueError('The state transition has already been made')
        previous_state = self.state
        previous_comment = self.comment
        if (new_state == previous_state):
            # If the new state is the same as the previous state, raise a ValueError
            raise ValueError('You cannot transition to the same state')

        self.state = new_state
        self.comment = comment
        self.current_state_start = timezone.now()
        self.save()

        # Create a new snapshot of the contract request
        ContractRequestSnapshot.objects.create(
            contract_request=self,
            state=previous_state,
            state_start=self.current_state_start,
            state_end=timezone.now(),
            comment=previous_comment
        )

        return previous_state
    
    def assign_to(self, user):
        # Assign the contract request to a user
        self.assigned_to = user
        self.save()

class ContractRequestSnapshot(models.Model):
    # Contract Request Snapshot model
    contract_request = models.ForeignKey(ContractRequest, on_delete=models.CASCADE)
    state = models.CharField(max_length=64)
    state_start = models.DateTimeField()
    state_end = models.DateTimeField()
    comment = models.TextField(null=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                # Ensure that there is only one snapshot for each state of a contract request
                fields=['contract_request', 'state'], name='unique_contract_request_snapshot')
        ]

    def __str__(self):
        return str(self.id)