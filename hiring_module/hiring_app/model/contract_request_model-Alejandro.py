import uuid
from django.db import models
from .user_model import CustomUser
from django.utils import timezone
from .contract_request_snapshot_model import ContractRequestSnapshot

# Description: Defines the choices for the state field in ContractRequest model.
# Input: None
# Output: Tuple of state choices.
def state_choices():
    return (
        ('pending', 'Pending'),
        ('review', 'Review'),
        ('incomplete', 'Incomplete'),
        ('filed', 'Filed'),
        ('cancelled', 'Cancelled')
    )

# Description: Abstract model class for contract requests.
# Input: None
# Output: None
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

    class Meta:
        abstract = True

    # Description: String representation of the ContractRequest instance.
    # Input: None
    # Output: String representation of the instance.
    def __str__(self):
        return str(self.id)

    # Description: Get snapshots related to the ContractRequest instance.
    # Input: None
    # Output: Queryset of related snapshots.
    def get_snapshots(self):
        return ContractRequestSnapshot.objects.filter(contract_request_id=self.id)

    # Description: Edit the comment of the current snapshot of the contract request.
    # Input: New comment.
    # Output: None
    def edit_comment(self, comment):
        current_snapshot = self.get_snapshots().filter(state=self.state).first()
        current_snapshot.comment = comment
        current_snapshot.save()

    # Description: Transition the contract request to a new state.
    # Input: New state, optional comment.
    # Output: Previous state.
    def transition_to_state(self, new_state, comment=''):
        if new_state not in dict(state_choices()).keys():
            raise ValueError('Invalid state provided')
        snapshots = self.get_snapshots()
        if (snapshots.filter(state=new_state).count() >= 1):
            raise ValueError('The state transition has already been made')
        previous_state = self.state
        if (new_state == previous_state):
            raise ValueError('You cannot transition to the same state')

        self.state = new_state
        self.current_state_start = timezone.now()
        self.save()
        self.create_snapshot(comment=comment)
        return previous_state

    # Description: Assign a leader to the contract request.
    # Input: User to assign as leader.
    # Output: None
    def assign_leader(self, user):
        self.leader_assigned_to = user
        self.save()

    # Description: Assign a manager to the contract request.
    # Input: User to assign as manager.
    # Output: None
    def assign_manager(self, user):
        self.manager_assigned_to = user
        self.save()

    # Description: Check if the transition to the new state is valid.
    # Input: New state.
    # Output: Boolean indicating validity of transition.
    def is_valid_transition(self, new_state):
        transitions = {
            'pending': ('review', 'incomplete', 'cancelled'),
            'review': ('filed', 'cancelled'),
            'incomplete': ('review', 'cancelled'),
            'filed': (),
            'cancelled': ()
        }

        return new_state in transitions.get(self.state, ())

    # Description: Create a snapshot of the current state of the contract request.
    # Input: Old state (optional), comment.
    # Output: Created snapshot instance.
    def create_snapshot(self, old_state=None, comment=''):
        if(old_state is not None):
            previous_snapshot = self.get_snapshots().filter(state=old_state).first()
            if previous_snapshot:
                previous_snapshot.state_end = timezone.now()
                previous_snapshot.save()

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
