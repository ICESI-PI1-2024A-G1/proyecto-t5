from django import forms
class LoginForm(forms.Form):
    id = forms.IntegerField(label='Usuario', widget=forms.TextInput(attrs={'class': 'rounded-r-lg border border-[#B8B8B8] pl-2 pr-2 w-60 h-10 focus:outline-none', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'rounded-r-lg border border-[#B8B8B8] pl-2 pr-8 w-60 h-10 focus:outline-none', 'placeholder': 'Contraseña'}))
