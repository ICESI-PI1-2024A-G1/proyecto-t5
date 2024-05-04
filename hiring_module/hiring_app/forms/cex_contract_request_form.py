from django import forms
from hiring_app.model import CEXContractRequest

class CEXContractRequestForm(forms.ModelForm):
    class Meta:
        model = CEXContractRequest
        fields = '__all__'