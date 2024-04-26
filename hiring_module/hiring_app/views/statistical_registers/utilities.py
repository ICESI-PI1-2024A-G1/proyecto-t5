from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse

# Decorador para redirigir a los líderes a la página de estadísticas del manager
def leader_redirect_to_manager_statistics(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name='leader').exists():
            # Si el usuario es un líder, lo redirigimos a la página de estadísticas del manager
            return redirect('hiring_app:manager_statistics')
        
        # Si no es líder, llamamos a la vista original
        return view_func(request, *args, **kwargs)
    
    return wrapper
