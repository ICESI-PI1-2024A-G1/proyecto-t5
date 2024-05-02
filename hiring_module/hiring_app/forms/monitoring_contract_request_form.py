from django import forms
from hiring_app.model import MonitoringContractRequest

# Description: Form class for monitoring contract requests.
# Input: None
# Output: None
class MonitoringContractRequestForm(forms.ModelForm):
    class Meta:
        model = MonitoringContractRequest
        fields = '__all__'