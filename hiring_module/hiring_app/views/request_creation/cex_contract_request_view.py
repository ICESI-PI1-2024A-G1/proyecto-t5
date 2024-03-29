from django.views.generic import CreateView
from hiring_app.forms import CEXContractRequestForm
from hiring_app.model import CEXContractRequest
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from .utilities import utilities

class CEXContractRequestView(CreateView):
    model = CEXContractRequest
    form_class = CEXContractRequestForm
    success_url = reverse_lazy('hiring_app:cex')
    template_name = 'request_creation/cex_request_form.html'

    def form_valid(self, form):
        # Assign created_by and estimated_completion_date fields
        current_user = self.request.user
        estimated_completion_date = datetime.now() + timedelta(days=30)
        form.instance.estimated_completion_date = estimated_completion_date
        form.instance.created_by = current_user

        utilities.sendEmailSuccess(current_user)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))