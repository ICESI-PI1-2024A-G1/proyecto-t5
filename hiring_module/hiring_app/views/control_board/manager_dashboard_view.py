from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

def manager_required(view_func):
    def wrapper(request, *args, **kwargs):
        # Check if the user is a manager, if not redirect to the appropriate dashboard
        if not request.user.groups.filter(name='Manager').exists():
            if request.user.groups.filter(name='Administrator').exists():
                return redirect('hiring_app:administrator_dashboard')
            elif request.user.groups.filter(name='Leader').exists():
                return redirect('hiring_app:leader_dashboard')
            else:
                return redirect('hiring_app:external_user_dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper

class ManagerDashboardView(TemplateView):
    template_name = 'manager_dashboard.html'

    @method_decorator(manager_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)