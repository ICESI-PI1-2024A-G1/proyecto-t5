from django import forms

class LoginForm(forms.Form):
    id = forms.IntegerField(label='Usuario', widget=forms.TextInput(attrs={'style': 'border-radius: 0.25rem; border: 1px solid #b8b8b8; padding: 0.25rem 0.5rem; width: 15rem; height: 2.5rem; outline: none;', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'border-radius: 0.25rem; border: 1px solid #b8b8b8; padding: 0.25rem 1rem 0.25rem 0.5rem; width: 15rem; height: 2.5rem; outline: none;', 'placeholder': 'Contraseña'}))
