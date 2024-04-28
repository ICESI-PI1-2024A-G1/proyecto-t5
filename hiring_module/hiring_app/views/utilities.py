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

    approved_requests = CEXContractRequest.objects.filter(state='filed').count() + MonitoringContractRequest.objects.filter(state='filed').count()
    review_requests = CEXContractRequest.objects.filter(state='review').count() + MonitoringContractRequest.objects.filter(state='review').count()
    for_validate_requests = CEXContractRequest.objects.filter(state='pending').count() + MonitoringContractRequest.objects.filter(state='pending').count()
    for_validate_requests += CEXContractRequest.objects.filter(state='incomplete').count() + MonitoringContractRequest.objects.filter(state='incomplete').count()

    
    

    return {
        'approved_requests': approved_requests,
        'review_requests': review_requests,
        'for_validate_requests': for_validate_requests,
    }
