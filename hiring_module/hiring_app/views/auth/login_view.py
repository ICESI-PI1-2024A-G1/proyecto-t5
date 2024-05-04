from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from django.urls import reverse_lazy
from hiring_app.forms import LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Description: View for handling user login.
# Input: FormView, request, *args, **kwargs
# Output: HttpResponseRedirect or render template
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('hiring_app:external_user_dashboard')

    # Description: Redirect the user to the corresponding dashboard based on their role.
    # Input: user (CustomUser object)
    # Output: Reverse_lazy object (URL)
    @staticmethod
    def user_authenticated_redirect(user):
        if user.groups.filter(name='admin').exists():
            return reverse_lazy('hiring_app:administrator_dashboard')
        elif user.groups.filter(name='leader').exists():
            return reverse_lazy('hiring_app:leader_dashboard')
        elif user.groups.filter(name='manager').exists():
            return reverse_lazy('hiring_app:manager_dashboard')
        else:
            return reverse_lazy('hiring_app:external_user_dashboard')

    # Description: Redirect the user to the corresponding dashboard if they are already authenticated.
    # Input: request, *args, **kwargs
    # Output: HttpResponseRedirect or render template
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.user_authenticated_redirect(request.user))
        return super().dispatch(request, *args, **kwargs)

    # Description: Authenticate the user and redirect them to the corresponding dashboard.
    # Input: form (LoginForm instance)
    # Output: HttpResponseRedirect or render template
    def form_valid(self, form):
        id = form.cleaned_data['id']
        password = form.cleaned_data['password']

        user = authenticate(request=self.request, id=id, password=password)

        if user is not None:
            login(self.request, user)
            return redirect(self.user_authenticated_redirect(user))

        messages.error(self.request, 'Credenciales incorrectas. Por favor, inténtelo de nuevo.')
        return HttpResponseRedirect(reverse_lazy('login'))

