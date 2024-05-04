from django.http import Http404, HttpResponse
from django.views.generic import CreateView
from hiring_app.forms import ProvisionOfServicesContractRequestForm
from hiring_app.model import ProvisionOfServicesContractRequest
from hiring_app.model import CourseSchedule
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from .utilities import utilities
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

# Description: View for creating Provision of Services contract requests.
# Input: Inherits from CreateView.
# Output: Renders Provision of Services contract request form and handles form submission.
class POSContractRequestView(CreateView):
    model = ProvisionOfServicesContractRequest
    form_class = ProvisionOfServicesContractRequestForm
    success_url = reverse_lazy('hiring_app:pos')
    template_name = 'request_creation/pos_request_form.html'

    # Description: Handles form submission when form data is valid.
    # Input: form (ProvisionOfServicesContractRequestForm): The validated form instance.
    # Output: Redirects to success URL after saving the form data.
    def form_valid(self, form):
        current_user = self.request.user
        estimated_completion_date = datetime.now() + timedelta(days=30)
        leader = utilities.findLeaderToAssign()
        manager = utilities.findManagerToAssign()
        form.instance.estimated_completion_date = estimated_completion_date
        form.instance.created_by = current_user
        form.instance.leader_assigned_to = leader
        form.instance.manager_assigned_to = manager

        pos_contract_request = form.save(commit=False)
        pos_contract_request.create_snapshot()
        pos_contract_request.save()
        additional_fields = {}
        for key, value in self.request.POST.items():
            if key.startswith('additionalFields-'):
                field_name = key.replace('additionalFields-', '')
                field_name = field_name.split('-')[0]
                additional_fields[field_name] = value
                if(field_name == 'responsability'):
                    additional_fields['pos_contract_request'] = pos_contract_request
                    course_schedule = CourseSchedule.objects.create_schedule(**additional_fields)
                    course_schedule.save()
                    additional_fields = {}
        utilities.send_email('Solicitud de contratación radicada', 'Estimado/a, su solicitud de contrato en el aplicativo del módulo de contratación de la unidad de servicios compartidos ha sido radicada satisfactoriamente',
                   "alejandrolonber25@gmail.com")
        return super().form_valid(form)
    
    # Description: Handles form submission when form data is invalid.
    # Input: form (ProvisionOfServicesContractRequestForm): The invalid form instance.
    # Output: Renders the form again with validation errors.
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    

    
# Description: Downloads the RUT file associated with a Provision of Services contract request.
# Input: idContract (int): The ID of the Provision of Services contract request.
# Output: HttpResponse: Response containing the RUT file.
def download_rut_file(request, idContract, *args, **kwargs):
    model_instance = get_object_or_404(ProvisionOfServicesContractRequest, id=idContract)
    if not request.user.has_perm('your_app.view_poscontractrequest'):
        raise PermissionDenied("You don't have permission to download this file.")

    if not model_instance.rut:
        raise Http404("The requested file does not exist.")
    try:
        rut_file_data = model_instance.rut
    except IOError as e:
        raise IOError(f"Error reading file: {e}")

    response = HttpResponse(rut_file_data, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{model_instance.rut.name}"'
    return response