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
         # Assign created_by and estimated_completion_date fields
        current_user = self.request.user
        estimated_completion_date = datetime.now() + timedelta(days=15)
        form.instance.estimated_completion_date = estimated_completion_date
        form.instance.created_by = current_user
            
        utilities.sendEmailSuccess(current_user)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))