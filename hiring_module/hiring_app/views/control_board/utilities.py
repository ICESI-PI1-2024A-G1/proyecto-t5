from functools import wraps
from django.shortcuts import redirect

# Decorator to redirect users to the correct dashboard based on their role
def role_redirect(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Check if the user is already on the correct dashboard
        if request.user.groups.filter(name='admin').exists() and request.path != '/hiring_app/administrator_dashboard/':
            return redirect('hiring_app:administrator_dashboard')
        elif request.user.groups.filter(name='leader').exists() and request.path != '/hiring_app/leader_dashboard/':
            return redirect('hiring_app:leader_dashboard')
        elif request.user.groups.filter(name='manager').exists() and request.path != '/hiring_app/manager_dashboard/':
            return redirect('hiring_app:manager_dashboard')
        elif not request.user.groups.exists() and request.path != '/hiring_app/external_user_dashboard/':
            return redirect('hiring_app:external_user_dashboard')
        
        # Call the original view function if no redirection is needed
        return view_func(request, *args, **kwargs)
    
    return wrapper

# Decorator to ensure that only users with the 'admin' role can access a view
def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.groups.filter(name='admin').exists():
            if request.user.groups.filter(name='leader').exists():
                return redirect('hiring_app:leader_dashboard')
            elif request.user.groups.filter(name='manager').exists():
                return redirect('hiring_app:manager_dashboard')
            else:
                return redirect('hiring_app:external_user_dashboard')
        return view_func(request, *args, **kwargs)
    
    return wrapper

# Decorator to ensure that only users with the 'leader' role can access a view
def leader_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.groups.filter(name='leader').exists():
            if request.user.groups.filter(name='admin').exists():
                return redirect('hiring_app:administrator_dashboard')
            elif request.user.groups.filter(name='manager').exists():
                return redirect('hiring_app:manager_dashboard')
            else:
                return redirect('hiring_app:external_user_dashboard')
        return view_func(request, *args, **kwargs)
    
    return wrapper

# Decorator to ensure that only users with the 'manager' role can access a view
def manager_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.groups.filter(name='manager').exists():
            if request.user.groups.filter(name='admin').exists():
                return redirect('hiring_app:administrator_dashboard')
            elif request.user.groups.filter(name='leader').exists():
                return redirect('hiring_app:leader_dashboard')
            else:
                return redirect('hiring_app:external_user_dashboard')
        return view_func(request, *args, **kwargs)
    
    return wrapper