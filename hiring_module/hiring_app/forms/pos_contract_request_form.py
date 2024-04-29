from django import forms
from hiring_app.model import ProvisionOfServicesContractRequest

class ProvisionOfServicesContractRequestForm(forms.ModelForm):
    class Meta:
        model = ProvisionOfServicesContractRequest
        fields = '__all__'