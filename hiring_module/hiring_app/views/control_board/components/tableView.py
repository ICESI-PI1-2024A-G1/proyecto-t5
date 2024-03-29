from django.views.generic import ListView
from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest

class SolicitudListView(ListView):
    template_name = 'hiring_app/administrator_dashboard.html'
    context_object_name = 'solicitudes'

    def get_queryset(self):
        solicitudes = self.get_all_solicitudes()
        solicitudes_sorted = sorted(solicitudes, key=lambda x: x.completion_date, reverse=True)
        return solicitudes_sorted

    def get_all_solicitudes(self):
        solicitudes_cex = CEXContractRequest.objects.all()
        solicitudes_monitoring = MonitoringContractRequest.objects.all()
        return list(solicitudes_cex) + list(solicitudes_monitoring)
