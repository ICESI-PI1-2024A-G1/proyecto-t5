from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from django.urls import reverse_lazy
from hiring_app.forms import LoginForm
from django.http import HttpResponseRedirect

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('hiring_app:control_board')

    def form_valid(self, form):
        id = form.cleaned_data['id']
        password = form.cleaned_data['password']
        
        user = authenticate(request=self.request, id=id, password=password)
        
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Credenciales incorrectas. Por favor, inténtelo de nuevo.')
            return HttpResponseRedirect(reverse_lazy('login')) 
