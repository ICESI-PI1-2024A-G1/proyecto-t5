from django.views.generic.edit import CreateView
from hiring_app.forms import MonitoringContractRequestForm
from hiring_app.model import MonitoringContractRequest
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from .utilities import utilities

class MonitoringContractRequestView(CreateView):
    model = MonitoringContractRequest
    form_class = MonitoringContractRequestForm
    template_name = 'request_creation/monitoring_request_form.html'
    success_url = reverse_lazy('hiring_app:monitoring') 

    def form_valid(self, form):
        # Assign created_by, estimated_completion_date and responsibles fields
        current_user = self.request.user
        estimated_completion_date = datetime.now() + timedelta(days=15)
        leader = utilities.findLeaderToAssign()
        manager = utilities.findManagerToAssign()
        form.instance.estimated_completion_date = estimated_completion_date
        form.instance.created_by = current_user
        form.instance.leader_assigned_to = leader
        form.instance.manager_assigned_to = manager
        
        monitoring_contract_request = form.save(commit=False)
        monitoring_contract_request.create_snapshot()
        monitoring_contract_request.save()
            
            
        utilities.send_email('Solicitud de contratación radicada', 'Estimado/a, su solicitud de contrato en el aplicativo del módulo de contratación de la unidad de servicios compartidos ha sido radicada satisfactoriamente',
                   current_user.email)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actualgroup'] = 'external'
        return context