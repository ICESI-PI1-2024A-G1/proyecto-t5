from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from hiring_app.views.control_board.utilities import role_redirect

class ManagerDashboardView(TemplateView):
    template_name = 'manager_dashboard.html'

    @method_decorator(role_redirect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
