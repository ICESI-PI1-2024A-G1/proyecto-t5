from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

def leader_required(view_func):
    def wrapper(request, *args, **kwargs):
        # Check if the user is a leader, if not redirect to the appropriate dashboard
        if not request.user.groups.filter(name='leader').exists():
            if request.user.groups.filter(name='admin').exists():
                return redirect('hiring_app:administrator_dashboard')
            elif request.user.groups.filter(name='manager').exists():
                return redirect('hiring_app:manager_dashboard')
            else:
                return redirect('hiring_app:external_user_dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper

class LeaderDashboardView(TemplateView):
    template_name = 'leader_dashboard.html'

    @method_decorator(leader_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)