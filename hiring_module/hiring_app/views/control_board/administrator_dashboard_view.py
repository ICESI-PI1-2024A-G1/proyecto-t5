from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        # Check if the user is an administrator, if not redirect to the appropriate dashboard
        if not request.user.groups.filter(name='admin').exists():
            if request.user.groups.filter(name='leader').exists():
                return redirect('hiring_app:leader_dashboard')
            elif request.user.groups.filter(name='manager').exists():
                return redirect('hiring_app:manager_dashboard')
            else:
                return redirect('hiring_app:external_user_dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper


class AdministratorDashboardView(TemplateView):
    template_name = 'administrator_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the first name and last name of the logged-in user
        first_name = self.request.user.first_name
        last_name = self.request.user.last_name
        # Get the first word of the first name and last name
        first_name = first_name.split()[0]
        last_name = last_name.split()[0]
        # Pass the first name and last name to the context
        context['user_first_name'] = first_name
        context['user_last_name'] = last_name
        # Retrieve contract requests
        solicitudes_cex = CEXContractRequest.objects.all()
        solicitudes_monitoring = MonitoringContractRequest.objects.all()
        # Combine both queries into a single list
        solicitudes = list(solicitudes_cex) + list(solicitudes_monitoring)
        # Pass the list of requests to the context
        context['solicitudes'] = solicitudes
        return context

