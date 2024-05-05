from django import forms

class NumberInput(forms.TextInput):
    input_type = 'number'

class LoginForm(forms.Form):
    id = forms.IntegerField(
        label='ID',
        widget=NumberInput(
            attrs={
                'style': 'padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px; font-size: 14px;',
                'placeholder': 'ID',
                'min': '0',  # Establece el valor mínimo permitido
                'step': '1', # Define el incremento/decremento
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
