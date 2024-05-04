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
    estimated_completion_date = models.DateField(null=True, blank=True)
    current_state_start = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=64, choices=state_choices(), default='pending', null=True, blank=True)
    manager_assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='manager_%(class)s_requests', null=True, blank=True)
    leader_assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='leader_%(class)s_requests', null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_%(class)s_requests', null=True, blank=True)
    transitions = {
            'pending': ('review', 'incomplete', 'cancelled'),
            'review': ('filed', 'cancelled'),
            'incomplete': ('review', 'cancelled'),
            'filed': (),
            'cancelled': ()
        }
    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)

    def get_snapshots(self):
        return ContractRequestSnapshot.objects.filter(contract_request_id=self.id)

    def edit_comment(self, comment):
        current_snapshot = self.get_snapshots().filter(state=self.state).first()
        current_snapshot.comment = comment
        current_snapshot.save()

    def transition_to_state(self, new_state, comment=''):
        print("Esto está pasando")

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
    

    def is_valid_transition(self, new_state):
        return new_state in self.transitions.get(self.state, ())
        
        
    def create_snapshot(self, old_state=None, comment=''):
        # Get the previous snapshot of the contract request
        if self.state is None:
            self.state = 'pending'
        if self.current_state_start is None:
            self.current_state_start = timezone.now()
        if(old_state is not None):
            previous_snapshot = self.get_snapshots().filter(state=old_state).first()
            if previous_snapshot:
                # If there is a previous snapshot, set the end date of the previous snapshot to the current date
                previous_snapshot.state_end = timezone.now()
                previous_snapshot.save()
        # Create a snapshot of the current state of the contract request
        # If it's filled or cancelled, set the end date to the current date
        if self.state in ['filed', 'cancelled']:
            state_end = timezone.now()
        else:
            state_end = None
        snapshot = ContractRequestSnapshot.objects.create(
            contract_request_id=self.id,
            state=self.state,
            state_start=self.current_state_start,
            state_end=state_end,
            comment=comment
        )

        snapshot.save()

        return snapshot
            


