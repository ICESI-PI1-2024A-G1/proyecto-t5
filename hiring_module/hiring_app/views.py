from django.shortcuts import render
from django.contrib.auth.views import LoginView

def login(request, **kwargs):
    return LoginView.as_view(template_name="auth/login.html")(request,**kwargs)

def home(request):
    return render(request, 'home.html')