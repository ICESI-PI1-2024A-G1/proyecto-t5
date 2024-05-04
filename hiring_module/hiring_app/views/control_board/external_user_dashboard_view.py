from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from functools import wraps
from django.shortcuts import redirect

# Description: Decorator to ensure both role and login requirements are met before accessing a view.
# Input: view_func (function): The view function to be wrapped.
# Output: The wrapped view function.
def role_and_login_required(view_func):

    # Description: Wrapper function to check login status and role before accessing the view.
    # Input: request, *args, **kwargs
    # Output: Redirects to the appropriate dashboard or home page if requirements are not met.
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        elif request.user.groups.filter(name='admin').exists() and request.path != '/hiring_app/administrator_dashboard/':
            return redirect('hiring_app:administrator_dashboard')
        elif request.user.groups.filter(name='leader').exists() and request.path != '/hiring_app/leader_dashboard/':
            return redirect('hiring_app:leader_dashboard')
        elif request.user.groups.filter(name='manager').exists() and request.path != '/hiring_app/manager_dashboard/':
            return redirect('hiring_app:manager_dashboard')
        elif not request.user.groups.exists() and request.path != '/hiring_app/external_user_dashboard/':
            return redirect('hiring_app:external_user_dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper

# Description: View for displaying the external user dashboard.
# Input: TemplateView
# Output: Renders the external user dashboard template.
class ExternalUserDashboardView(TemplateView):
    template_name = 'control_board/external_user_dashboard.html'

    # Description: Dispatch method to redirect based on user role and login status.
    # Input: self, *args, **kwargs
    # Output: Super dispatch method with redirection based on user role and login status.
    @method_decorator(role_and_login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
