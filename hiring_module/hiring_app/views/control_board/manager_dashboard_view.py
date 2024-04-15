from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from hiring_app.views.control_board.utilities import role_redirect
from hiring_app.views.control_board.general_dashboard_view import GeneralDashboard

class ManagerDashboardView(TemplateView, GeneralDashboard):
    template_name = 'control_board/manager_dashboard.html'

    # Redirect to correct dashboard based on user role
    @method_decorator(role_redirect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
