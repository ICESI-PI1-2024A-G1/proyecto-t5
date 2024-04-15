from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest

class GeneralDashboard():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        solicitudes_cex = CEXContractRequest.objects.all()
        solicitudes_monitoring = MonitoringContractRequest.objects.all()
        # Combine both queries into a single list
        solicitudes = list(solicitudes_cex) + list(solicitudes_monitoring)
        # Pass the list of requests to the context
        context['solicitudes'] = solicitudes
        return context