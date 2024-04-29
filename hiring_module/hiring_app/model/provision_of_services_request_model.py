from django.db import models
from .cex_contract_request_model import CEXContractRequest

class ProvisionOfServicesContractRequestManager(models.Manager):
    def create_contract_request(self, course_schedules, **extra_fields):
        from .course_schedule_model import CourseSchedule
        provision_of_services_request = self.create(
            **extra_fields
        )
        provision_of_services_request.create_snapshot()
        provision_of_services_request.save(using=self._db)
        for course_schedule_ in course_schedules:
            course_schedule = CourseSchedule.objects.create_schedule(
                pos_contract_request=provision_of_services_request,
                date=course_schedule_['date'],
                start_time=course_schedule_['start_time'],
                end_time=course_schedule_['end_time'],
                room=course_schedule_['room'],
                responsability=course_schedule_['responsability']
            )
            course_schedule.save()
        return provision_of_services_request
    
class ProvisionOfServicesContractRequest(CEXContractRequest):
    
    objects = ProvisionOfServicesContractRequestManager()
    
    course_name = models.CharField(max_length=256)
    period = models.CharField(max_length=64)
    group = models.CharField(max_length=2)
    intensity = models.IntegerField()
    total_hours = models.IntegerField()
    course_code = models.CharField(max_length=16)
    students_quantity = models.IntegerField()
    additional_hours = models.IntegerField()
    
    def clean(self):
        super().clean()
        
    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
