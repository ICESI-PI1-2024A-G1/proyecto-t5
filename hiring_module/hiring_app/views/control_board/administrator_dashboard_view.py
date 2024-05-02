from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest
from .utilities import role_redirect, get_requests

# Description: View for the administrator dashboard.
# Input: View
# Output: Renders the administrator dashboard template with context data.
class AdministratorDashboardView(View):
    template_name = 'control_board/administrator_dashboard.html'

    # Description: Dispatch method to redirect users based on their role.
    # Input: self, request, *args, **kwargs
    # Output: Renders the administrator dashboard template with context data.
    @method_decorator(role_redirect)
    def dispatch(self, request, *args, **kwargs):
        context = {
            'actualgroup': 'admin'
        }
        context.update(get_requests(self.request.user))
        return render(request, self.template_name, context)
    
    