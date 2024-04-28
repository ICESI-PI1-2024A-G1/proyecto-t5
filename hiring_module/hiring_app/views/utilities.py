from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse
from hiring_app.model import CustomUser
from django.contrib.auth.models import Group
from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest

# Decorator to redirect leaders and administrators to manager statistics page


def leader_or_admin_redirect_to_manager_statistics(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # If the user is not authenticated, redirect the user to login
            return redirect('login')

        if request.user.groups.filter(name__in=['leader', 'admin']).exists():
            # If the user is a leader or administrator, and is not on the manager statistics page, redirect them there
            if not request.path == reverse('hiring_app:manager_statistics'):
                return redirect('hiring_app:manager_statistics')

        # If the user is not a leader or administrator, or the leader or administrator already on the manager’s statistics page, call the original view
        return view_func(request, *args, **kwargs)

    return wrapper


def get_metrics():
    approved_requests = 0
    review_requests = 0
    for_validate_requests = 0
    managers = CustomUser.objects.filter(
        groups=Group.objects.get(name='manager'))
    data = []
    best_to_worse_manager = []

    for manager in managers:
        cex_requests = CEXContractRequest.objects.filter(
            manager_assigned_to=manager)
        
        monitoring_requests = MonitoringContractRequest.objects.filter(
            manager_assigned_to=manager)
        
        
        approved_requests = cex_requests.filter(state='filed').count(
        ) + monitoring_requests.filter(state='filed').count()
        
        
        review_requests = cex_requests.filter(state='review').count(
        ) + monitoring_requests.filter(state='review').count()
        
        
        for_validate_requests = cex_requests.filter(state='pending').count(
        ) + monitoring_requests.filter(state='pending').count()
        
        
        for_validate_requests += cex_requests.filter(state='incomplete').count(
        ) + monitoring_requests.filter(state='incomplete').count()
        
        
        data.append([(manager.first_name + ' ' + manager.last_name), approved_requests,
                    review_requests, for_validate_requests])
        
        
        best_to_worse_manager.append([(manager.first_name + ' ' + manager.last_name), quality_calculator(approved_requests, review_requests, for_validate_requests)])

    best_to_worse_manager = sorted(best_to_worse_manager, key=lambda x: x[1], reverse=True)

    return {
        'data': data,
        'quality': best_to_worse_manager
    }

def quality_calculator(aprobadas, en_revision, por_validar):
    total = aprobadas + en_revision + por_validar

    if total != 0:
        porcentaje_aprobadas = (aprobadas / total) * 100
        porcentaje_aprobadas = round(porcentaje_aprobadas, 2)
        return porcentaje_aprobadas
    else:
        return 0 
