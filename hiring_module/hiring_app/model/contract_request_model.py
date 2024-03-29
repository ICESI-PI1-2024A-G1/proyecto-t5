import uuid
from django.db import models
from .user_model import CustomUser
from django.utils import timezone
from .contract_request_snapshot_model import ContractRequestSnapshot

def state_choices():
    return (
        ('pending', 'Pending'),
        ('review', 'Review'),
        ('incomplete', 'Incomplete'),
        ('filed', 'Filed'),
        ('cancelled', 'Cancelled')
    )

class ContractRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_date = models.DateField(auto_now_add=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    estimated_completion_date = models.DateField()
    current_state_start = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=64, choices=state_choices(), default='pending')
    manager_assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='manager_%(class)s_requests', null=True, blank=True)
    leader_assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='leader_%(class)s_requests', null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_%(class)s_requests')

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)

    def get_snapshots(self):
        # Get all snapshots of the contract request
        return ContractRequestSnapshot.objects.filter(contract_request_id=self.id)

    def edit_comment(self, comment):
        # Edit the comment of the current snapshot of the contract request
        current_snapshot = self.get_snapshots().filter(state=self.state).first()
        current_snapshot.comment = comment
        current_snapshot.save()

    def transition_to_state(self, new_state, comment=''):
        # Transition the contract request to a new state
        # If the new state is not valid, raise a ValueError
        if new_state not in dict(state_choices()).keys():
            raise ValueError('Invalid state provided')
        snapshots = self.get_snapshots()
        if (snapshots.filter(state=new_state).count() >= 1):
            # If the state transition has already been made, raise a ValueError
            raise ValueError('The state transition has already been made')
        previous_state = self.state
        if (new_state == previous_state):
            # If the new state is the same as the previous state, raise a ValueError
            raise ValueError('You cannot transition to the same state')

        self.state = new_state
        self.current_state_start = timezone.now()
        self.save()
        self.create_snapshot(comment=comment)
        return previous_state

    def assign_leader(self, user):
        self.leader_assigned_to = user
        self.save()

    def assign_manager(self, user):
        self.manager_assigned_to = user
        self.save()

    def is_valid_transition(self, current_state, new_state):
        transitions = {
            'pending': ('review', 'incomplete', 'cancelled'),
            'review': ('filed', 'cancelled'),
            'incomplete': ('review', 'cancelled'),
            'filed': (),
            'cancelled': ()
        }

        return True
    
    def create_snapshot(self, comment=''):
        snapshot = ContractRequestSnapshot.objects.create(
            contract_request_id=self.id,
            state=self.state,
            state_start=self.current_state_start,
            state_end=timezone.now(),
            comment=comment
        )

        snapshot.save()

        return snapshot