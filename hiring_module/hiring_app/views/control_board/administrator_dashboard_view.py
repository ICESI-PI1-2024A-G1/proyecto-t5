from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest
from .general_dashboard_view import GeneralDashboard
from .utilities import role_redirect



class AdministratorDashboardView(TemplateView, GeneralDashboard):
    template_name = 'control_board/administrator_dashboard.html'

    # Redirect to correct dashboard based on user role
    @method_decorator(role_redirect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

