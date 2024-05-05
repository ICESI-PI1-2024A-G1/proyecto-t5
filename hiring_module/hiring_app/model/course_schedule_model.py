from django.db import models
from .provision_of_services_request_model import ProvisionOfServicesContractRequest

class CourseScheduleManager(models.Manager):
    def create_schedule(self, **extra_fields):
        # Create a CEX contract request
        schedule = self.create(
            **extra_fields
        )
        schedule.save(using=self._db)
        return schedule
    
class CourseSchedule(models.Model):
    
    objects = CourseScheduleManager()

    pos_contract_request = models.ForeignKey(ProvisionOfServicesContractRequest, on_delete=models.CASCADE, related_name='course_schedule')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=64)
    responsability = models.CharField(max_length=64)
    
    def clean(self):
        super().clean()
        
    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
