from django.contrib import admin
from .models import CustomUser, ContractRequestSnapshot, CEXContractRequest, MonitoringContractRequest

admin.site.register(CustomUser)
admin.site.register(ContractRequestSnapshot)
admin.site.register(CEXContractRequest)
admin.site.register(MonitoringContractRequest)