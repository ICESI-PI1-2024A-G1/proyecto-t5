from django.db import models
from .provision_of_services_request_model import ProvisionOfServicesContractRequest

# Description: Manager class for CourseSchedule instances.
# Input: None
# Output: None
class CourseScheduleManager(models.Manager):

    # Description: Creates a new CourseSchedule instance.
    # Input: Keyword arguments for additional fields.
    # Output: New CourseSchedule instance.
    def create_schedule(self, **extra_fields):
        schedule = self.create(
            **extra_fields
        )
        schedule.save(using=self._db)
        return schedule

# Description: Model class for course schedules.
# Input: None
# Output: None
class CourseSchedule(models.Model):
    objects = CourseScheduleManager()
    pos_contract_request = models.ForeignKey(ProvisionOfServicesContractRequest, on_delete=models.CASCADE, related_name='course_schedule')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=64)
    responsability = models.CharField(max_length=64)

    # Description: Clean method to validate model fields.
    # Input: None
    # Output: None
    def clean(self):
        super().clean()

    # Description: Save method to ensure validation before saving.
    # Input: None
    # Output: None
    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)

    # Description: String representation of the CourseSchedule instance.
    # Input: None
    # Output: String representation of the instance.
    def __str__(self):
        return str(self.id)
