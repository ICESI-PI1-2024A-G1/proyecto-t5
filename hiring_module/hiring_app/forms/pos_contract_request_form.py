from django import forms
from hiring_app.model import ProvisionOfServicesContractRequest

# Description: Form class for provision of services contract requests.
# Input: None
# Output: None
class ProvisionOfServicesContractRequestForm(forms.ModelForm):
    class Meta:
        model = ProvisionOfServicesContractRequest
        fields = '__all__'