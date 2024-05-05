from django import forms
from hiring_app.model import MonitoringContractRequest

class MonitoringContractRequestForm(forms.ModelForm):
    class Meta:
        model = MonitoringContractRequest
        fields = '__all__'