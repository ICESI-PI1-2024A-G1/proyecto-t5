from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

def role_redirect(view_func):
    def wrapper(request, *args, **kwargs):
        # Redirect to the appropriate dashboard based on the user's role
        if request.user.groups.filter(name='Administrator').exists():
            return redirect('hiring_app:administrator_dashboard')
        elif request.user.groups.filter(name='Leader').exists():
            return redirect('hiring_app:leader_dashboard')
        elif request.user.groups.filter(name='Manager').exists():
            return redirect('hiring_app:manager_dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper

class ExternalUserDashboardView(TemplateView):
    template_name = 'hiring_app/external_user_dashboard.html'
    @method_decorator(role_redirect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)