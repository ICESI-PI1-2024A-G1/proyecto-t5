from django import forms
from hiring_module.hiring_app.model.contract_request_model import ContractRequest

class ChangeStateForm(forms.ModelForm):

    # Description: Meta class to specify the model and fields for the form.
    # Input: None
    # Output: None
    class Meta:
        model = ContractRequest
        fields = ['state']
