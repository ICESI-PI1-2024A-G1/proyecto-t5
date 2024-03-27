from django import forms

from hiring_module.hiring_app.model.contract_request_model import ContractRequest

class ChangeStateForm(forms.ModelForm):
    class Meta:
        model = ContractRequest
        fields = ['state']
