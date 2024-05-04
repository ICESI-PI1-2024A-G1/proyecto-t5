from django.contrib import admin
from .model import CustomUser, ContractRequestSnapshot, CEXContractRequest, MonitoringContractRequest, ProvisionOfServicesContractRequest, CourseSchedule

# Description: Admin configuration for managing custom user accounts and contract requests.
# Input: None
# Output: None
class CustomUserAdmin(admin.ModelAdmin):

    # Description: Saves the custom user model instance with hashed password if password field is provided.
    # Input: request (HttpRequest): The request object, obj (CustomUser): The custom user instance being saved, form (Form): The form instance being used, change (bool): Indicates whether the object is being changed.
    # Output: None
    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data and form.cleaned_data.get('password'):
            obj.set_password(form.cleaned_data['password'])
        obj.save()

admin.site.register(ContractRequestSnapshot)
admin.site.register(CEXContractRequest)
admin.site.register(MonitoringContractRequest)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ProvisionOfServicesContractRequest)
admin.site.register(CourseSchedule)