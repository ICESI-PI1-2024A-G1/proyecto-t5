from django import forms
class LoginForm(forms.Form):
    id = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
