from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse
from hiring_app.model import CustomUser
from django.contrib.auth.models import Group
from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest
from hiring_app.model.provision_of_services_request_model import ProvisionOfServicesContractRequest
from collections import defaultdict
from datetime import datetime

# Description: Decorator to redirect leaders and administrators to the manager statistics page.
# Input: view_func (function): The view function to be wrapped.
# Output: Function object.
def leader_or_admin_redirect_to_manager_statistics(view_func):

    # Description: Wrapper function to redirect leaders and administrators to the manager statistics page.
    # Input: request (HttpRequest): The request object.
    # Output: The original view function or a redirect to the manager statistics page.
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        if request.user.groups.filter(name__in=['leader', 'admin']).exists():
            if not request.path == reverse('hiring_app:manager_statistics'):
                return redirect('hiring_app:manager_statistics')

        return view_func(request, *args, **kwargs)

    return wrapper

# Description: Retrieve metrics for manager statistics.
# Input: None
# Output: Dictionary containing metrics data.
def get_metrics():
    approved_requests = 0
    review_requests = 0
    for_validate_requests = 0
    managers = CustomUser.objects.filter(
        groups=Group.objects.get(name='manager'))
    cex_requests_ammount = 0
    monitoring_request_ammount = 0
    pos_requests_ammount = 0
    data = []
    best_to_worse_manager = []
    daily_requests = []
    monthly_requests = []

    cex_requests = CEXContractRequest.objects.all()
    monitoring_requests = MonitoringContractRequest.objects.all()
    pos_requests = ProvisionOfServicesContractRequest.objects.all()

    requests_count_by_date = defaultdict(lambda: [0, 0, 0])

    for request_type, queryset in [("CEX", cex_requests), ("Monitoring", monitoring_requests), ("POS", pos_requests)]:
        for request in queryset:
            start_date = request.start_date
            requests_count_by_date[start_date][{"CEX": 0, "Monitoring": 1, "POS": 2}[request_type]] += 1

    daily_requests = [[date.strftime('%Y-%m-%d')] + counts for date, counts in requests_count_by_date.items()]

    daily_requests.sort()

    for manager in managers:
        cex_requests = CEXContractRequest.objects.filter(
            manager_assigned_to=manager)
        
        monitoring_requests = MonitoringContractRequest.objects.filter(
            manager_assigned_to=manager)
        
        pos_requests = ProvisionOfServicesContractRequest.objects.filter(
            manager_assigned_to=manager)
        
        
        approved_requests = cex_requests.filter(state='filed').count(
        ) + monitoring_requests.filter(state='filed').count(
        ) + pos_requests.filter(state='filed').count(
        )
        
        
        review_requests = cex_requests.filter(state='review').count(
        ) + monitoring_requests.filter(state='review').count(
        ) + pos_requests.filter(state='review').count(
        )
        
        
        for_validate_requests = cex_requests.filter(state='pending').count(
        ) + monitoring_requests.filter(state='pending').count(
        ) + pos_requests.filter(state='pending').count(
        )
        
        
        for_validate_requests += cex_requests.filter(state='incomplete').count(
        ) + monitoring_requests.filter(state='incomplete').count(
        ) + pos_requests.filter(state='incomplete').count(
        )
        
        
        data.append([(manager.first_name + ' ' + manager.last_name), approved_requests,
                    review_requests, for_validate_requests])
        
        
        best_to_worse_manager.append([(manager.first_name + ' ' + manager.last_name), quality_calculator(approved_requests, review_requests, for_validate_requests)])

    best_to_worse_manager = sorted(best_to_worse_manager, key=lambda x: x[1], reverse=True)

    best_to_worse_manager = best_to_worse_manager[:5]

    best_to_worse_manager_with_percentage = [(nombre, f"{porcentaje} %") for nombre, porcentaje in best_to_worse_manager]

    
    
    return {
        'data': data,
        'quality': best_to_worse_manager_with_percentage,
        'daily_requests': daily_requests,
        'monthly_requests': monthly_requests
    }

# Description: Calculate quality percentage based on approved, under review, and to be validated requests.
# Input: aprobadas (int): Number of approved requests.
#        en_revision (int): Number of requests under review.
#        por_validar (int): Number of requests to be validated.
# Output: Quality percentage (float).
def quality_calculator(aprobadas, en_revision, por_validar):
    total = aprobadas + en_revision + por_validar

    if total != 0:
        porcentaje_aprobadas = (aprobadas / total) * 100
        porcentaje_aprobadas = round(porcentaje_aprobadas, 2)
        return porcentaje_aprobadas
    else:
        return 0 
