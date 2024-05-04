from django.views.generic import ListView
from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest

# Description: View for displaying a list of solicitudes.
# Input: ListView
# Output: Rendered template with context data
class SolicitudListView(ListView):
    template_name = 'hiring_app/administrator_dashboard.html'
    context_object_name = 'solicitudes'

    # Description: Get queryset for solicitudes list view.
    # Input: self
    # Output: Queryset of solicitudes sorted by completion date
    def get_queryset(self):
        solicitudes = self.get_all_solicitudes()
        solicitudes_sorted = sorted(solicitudes, key=lambda x: x.completion_date, reverse=True)
        return solicitudes_sorted

    # Description: Get all solicitudes.
    # Input: self
    # Output: List of all solicitudes (CEX and monitoring)
    def get_all_solicitudes(self):
        solicitudes_cex = CEXContractRequest.objects.all()
        solicitudes_monitoring = MonitoringContractRequest.objects.all()
        return list(solicitudes_cex) + list(solicitudes_monitoring)
