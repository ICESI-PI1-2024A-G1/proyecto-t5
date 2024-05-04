from django.db import models

# Description: Model class for snapshots of contract requests.
# Input: None
# Output: None
class ContractRequestSnapshot(models.Model):
    contract_request_id = models.UUIDField()
    state = models.CharField(max_length=64)
    state_start = models.DateTimeField()
    state_end = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['contract_request_id', 'state'], name='unique_contract_request_snapshot')
        ]

    # Description: String representation of the ContractRequestSnapshot instance.
    # Input: None
    # Output: String representation of the instance.
    def __str__(self):
        return str(self.id)
