from django.contrib import admin
from .model import CustomUser, ContractRequestSnapshot, CEXContractRequest, MonitoringContractRequest, ProvisionOfServicesContractRequest, CourseSchedule

class CustomUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Check if the password field has been changed and if it's provided in plaintext
        if 'password' in form.changed_data and form.cleaned_data.get('password'):
            obj.set_password(form.cleaned_data['password'])
        obj.save()

admin.site.register(ContractRequestSnapshot)
admin.site.register(CEXContractRequest)
admin.site.register(MonitoringContractRequest)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ProvisionOfServicesContractRequest)
admin.site.register(CourseSchedule)