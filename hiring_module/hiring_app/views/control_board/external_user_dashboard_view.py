from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

def role_redirect(view_func):
    def wrapper(request, *args, **kwargs):
        # Redirect to the appropriate dashboard based on the user's role
        if request.user.groups.filter(name='admin').exists():
            return redirect('hiring_app:administrator_dashboard')
        elif request.user.groups.filter(name='leader').exists():
            return redirect('hiring_app:leader_dashboard')
        elif request.user.groups.filter(name='manager').exists():
            return redirect('hiring_app:manager_dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper

class ExternalUserDashboardView(TemplateView):
    template_name = 'external_user_dashboard.html'
    @method_decorator(role_redirect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the first name and last name of the logged-in user
        first_name = self.request.user.first_name
        last_name = self.request.user.last_name
        # Get the first word of the first name and last name
        first_name = first_name.split()[0]
        last_name = last_name.split()[0]
        # Pass the first name and last name to the context
        context['user_first_name'] = first_name
        context['user_last_name'] = last_name
        return context