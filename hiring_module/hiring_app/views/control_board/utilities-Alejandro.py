from functools import wraps
from django.shortcuts import redirect

# Description: Decorator function to redirect users based on their role.
# Input: view_func (function): The view function to be decorated.
# Output: wrapper function to handle redirection based on user role.
def role_redirect(view_func):

    # Description: Wrapper function to check user role and redirect accordingly.
    # Input: request, *args, **kwargs
    # Output: Redirects users to their respective dashboard based on role.
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name='admin').exists() and request.path != '/hiring_app/administrator_dashboard/':
            return redirect('hiring_app:administrator_dashboard')
        elif request.user.groups.filter(name='leader').exists() and request.path != '/hiring_app/leader_dashboard/':
            return redirect('hiring_app:leader_dashboard')
        elif request.user.groups.filter(name='manager').exists() and request.path != '/hiring_app/manager_dashboard/':
            return redirect('hiring_app:manager_dashboard')
        elif not request.user.groups.exists() and request.path != '/hiring_app/external_user_dashboard/':
            return redirect('hiring_app:external_user_dashboard')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper
