from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

def manager_required(view_func):
    def wrapper(request, *args, **kwargs):
        # Check if the user is a manager, if not redirect to the appropriate dashboard
        if not request.user.groups.filter(name='manager').exists():
            if request.user.groups.filter(name='admin').exists():
                return redirect('hiring_app:administrator_dashboard')
            elif request.user.groups.filter(name='leader').exists():
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