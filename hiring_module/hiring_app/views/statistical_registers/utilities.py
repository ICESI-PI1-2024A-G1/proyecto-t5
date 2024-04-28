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


def get_metrics(user):
    # Get all managers
    group_manager = Group.objects.get(name='manager')
    managers = CustomUser.objects.filter(groups=group_manager)

    total_requests = 0
    approved_requests = 0
    review_requests = 0
    for_validate_requests = 0
    best_manager = None
    max_approved_requests = 0
    all_requests_assigned_to_the_best_manager = 0

    # Count the requests assigned to each manager
    for manager in managers:
        # View requests assigned to this manager in CEXContractRequest
        cex_requests = CEXContractRequest.objects.filter(manager_assigned_to=manager)
        # View requests assigned to this manager in MonitoringContractRequest
        monitoring_requests = MonitoringContractRequest.objects.filter(manager_assigned_to=manager)

        # Merge the results of both type requests
        total_requests_for_a_manager = cex_requests.count() + monitoring_requests.count()
        approved_requests += cex_requests.filter(state='filed').count() + monitoring_requests.filter(state='filed').count()
        review_requests += cex_requests.filter(state='review').count() + monitoring_requests.filter(state='review').count()
        for_validate_requests += cex_requests.filter(state__in=['pending', 'incomplete']).count() + monitoring_requests.filter(state__in=['pending', 'incomplete']).count()

        total_requests += total_requests_for_a_manager

        if approved_requests > max_approved_requests:
            max_approved_requests = approved_requests
            best_manager = manager.first_name + ' ' + manager.last_name
            all_requests_assigned_to_the_best_manager = total_requests_for_a_manager

    if best_manager:
        effectiveness_percentage = (max_approved_requests / all_requests_assigned_to_the_best_manager) * 100
    else:
        effectiveness_percentage = 0

    # Return metrics
    return {
        'total_requests': total_requests,
        'approved_requests': approved_requests,
        'review_requests': review_requests,
        'for_validate_requests': for_validate_requests,
        'best_manager': best_manager,
        'effectiveness_percentage': effectiveness_percentage,
    }
