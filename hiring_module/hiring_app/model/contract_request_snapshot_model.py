from django.db import models

class ContractRequestSnapshot(models.Model):
    # Contract Request Snapshot model
    contract_request_id = models.UUIDField()
    state = models.CharField(max_length=64)
    state_start = models.DateTimeField()
    state_end = models.DateTimeField()
    comment = models.TextField(null=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                # Ensure that there is only one snapshot for each state of a contract request
                fields=['contract_request_id', 'state'], name='unique_contract_request_snapshot')
        ]

    def __str__(self):
        return str(self.id)