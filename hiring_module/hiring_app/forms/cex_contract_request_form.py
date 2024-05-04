from django import forms
from hiring_app.model import CEXContractRequest

class CEXContractRequestForm(forms.ModelForm):

    # Description: Meta class to specify the model and fields for the form.
    # Input: None
    # Output: None
    class Meta:
        model = CEXContractRequest
        fields = '__all__'