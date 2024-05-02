from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest
from .utilities import role_redirect

# Description: View for the administrator dashboard.
# Input: TemplateView
# Output: Renders the administrator dashboard template with context data.
class AdministratorDashboardView(TemplateView):
    template_name = 'administrator_dashboard.html'

    # Description: Dispatch method to redirect users based on their role.
    # Input: self, *args, **kwargs
    # Output: Redirects to the appropriate dashboard based on user's role.
    @method_decorator(role_redirect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # Description: Method to retrieve context data for rendering template.
    # Input: self, **kwargs
    # Output: Context data containing all contract requests.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        solicitudes_cex = CEXContractRequest.objects.all()
        solicitudes_monitoring = MonitoringContractRequest.objects.all()
        solicitudes = list(solicitudes_cex) + list(solicitudes_monitoring)
        context['solicitudes'] = solicitudes
        return context

