from django import forms

# Description: Custom input widget to specify input type as 'number'.
# Input: None
# Output: None
class NumberInput(forms.TextInput):
    input_type = 'number'

# Description: Form class for user login.
# Input: User ID input as an integer, password input as a string.
# Output: None
class LoginForm(forms.Form):
    id = forms.IntegerField(
        label='ID',
        widget=NumberInput(
            attrs={
                'style': 'padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px; font-size: 14px;',
                'placeholder': 'ID',
                'min': '0',
                'step': '1', 
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'style': 'padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px; font-size: 14px;',
                'placeholder': '••••••••'
            }
        )
    )
