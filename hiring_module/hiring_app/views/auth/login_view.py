from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from django.urls import reverse_lazy
from hiring_app.forms import LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('hiring_app:external_user_dashboard')

    @staticmethod
    def user_authenticated_redirect(user):
        # Redirect the user to the corresponding dashboard based on their role
        if user.groups.filter(name='admin').exists():
            return reverse_lazy('hiring_app:administrator_dashboard')
        elif user.groups.filter(name='leader').exists():
            return reverse_lazy('hiring_app:leader_dashboard')
        elif user.groups.filter(name='manager').exists():
            return reverse_lazy('hiring_app:manager_dashboard')
        else:
            return reverse_lazy('hiring_app:external_user_dashboard')

    def dispatch(self, request, *args, **kwargs):
        # Redirect the user to the corresponding dashboard if they are already authenticated
        if request.user.is_authenticated:
            return redirect(self.user_authenticated_redirect(request.user))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Authenticate the user and redirect them to the corresponding dashboard
        id = form.cleaned_data['id']
        password = form.cleaned_data['password']

        user = authenticate(request=self.request, id=id, password=password)

        if user is not None:
            login(self.request, user)
            return redirect(self.user_authenticated_redirect(user))

        messages.error(self.request, 'Credenciales incorrectas. Por favor, inténtelo de nuevo.')
        return HttpResponseRedirect(reverse_lazy('login'))

