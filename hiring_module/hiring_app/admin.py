from django.contrib import admin
from .model import CustomUser, ContractRequestSnapshot, CEXContractRequest, MonitoringContractRequest

class CustomUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Hash the password if it's provided in plaintext
        if form.cleaned_data.get('password'):
            obj.set_password(form.cleaned_data['password'])
        obj.save()

admin.site.register(ContractRequestSnapshot)
admin.site.register(CEXContractRequest)
admin.site.register(MonitoringContractRequest)
admin.site.register(CustomUser, CustomUserAdmin)