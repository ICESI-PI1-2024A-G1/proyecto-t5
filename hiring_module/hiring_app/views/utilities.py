from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Avg, F, ExpressionWrapper, DurationField
from django.db.models import Q
from django.utils import timezone
from hiring_app.model import CustomUser
from datetime import timedelta
from django.contrib.auth.models import Group
from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest
from hiring_app.model.provision_of_services_request_model import ProvisionOfServicesContractRequest
from collections import defaultdict
from datetime import datetime

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


def get_manager_metrics():
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

    # Initialize a defaultdict to store requests count for each date
    requests_count_by_date = defaultdict(lambda: [0, 0, 0])

    # Iterate over each type of request
    for request_type, queryset in [("CEX", cex_requests), ("Monitoring", monitoring_requests), ("POS", pos_requests)]:
        for request in queryset:
            start_date = request.start_date
            requests_count_by_date[start_date][{"CEX": 0, "Monitoring": 1, "POS": 2}[request_type]] += 1

    # Convert the defaultdict to a list of lists
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
        
        cancelled_requests = cex_requests.filter(state='cancelled').count(
        ) + monitoring_requests.filter(state='cancelled').count(
        ) + pos_requests.filter(state='cancelled').count(
        )
        
        data.append([(manager.first_name + ' ' + manager.last_name), approved_requests,
                    review_requests, for_validate_requests,cancelled_requests])
        
        
        best_to_worse_manager.append([(manager.first_name + ' ' + manager.last_name), quality_calculator(approved_requests, review_requests, for_validate_requests,cancelled_requests)])

    best_to_worse_manager = sorted(best_to_worse_manager, key=lambda x: x[1], reverse=True)

    best_to_worse_manager = best_to_worse_manager[:5]

    best_to_worse_manager_with_percentage = [(nombre, f"{porcentaje} %") for nombre, porcentaje in best_to_worse_manager]
    
    overdue_requests = get_resolved_after_estimated_date()

    
    return {
        'manager_data': data,
        'manager_quality': best_to_worse_manager_with_percentage,
        'daily_requests': daily_requests,
        'monthly_requests': monthly_requests,
        'overdue_requests': overdue_requests
    }

def get_leader_metrics():
    approved_requests = 0
    review_requests = 0
    for_validate_requests = 0
    leaders = CustomUser.objects.filter(
        groups=Group.objects.get(name='leader'))
    
    cex_requests_ammount = 0
    monitoring_request_ammount = 0
    pos_requests_ammount = 0
    data = []
    best_to_worse_leader = []
    daily_requests = []
    monthly_requests = []

    cex_requests = CEXContractRequest.objects.all()
    monitoring_requests = MonitoringContractRequest.objects.all()
    pos_requests = ProvisionOfServicesContractRequest.objects.all()

    # Initialize a defaultdict to store requests count for each date
    requests_count_by_date = defaultdict(lambda: [0, 0, 0])

    # Iterate over each type of request
    for request_type, queryset in [("CEX", cex_requests), ("Monitoring", monitoring_requests), ("POS", pos_requests)]:
        for request in queryset:
            start_date = request.start_date
            requests_count_by_date[start_date][{"CEX": 0, "Monitoring": 1, "POS": 2}[request_type]] += 1

    # Convert the defaultdict to a list of lists
    daily_requests = [[date.strftime('%Y-%m-%d')] + counts for date, counts in requests_count_by_date.items()]

    daily_requests.sort()

    for leader in leaders:
        cex_requests = CEXContractRequest.objects.filter(
            leader_assigned_to=leader)
        
        monitoring_requests = MonitoringContractRequest.objects.filter(
            leader_assigned_to=leader)
        
        pos_requests = ProvisionOfServicesContractRequest.objects.filter(
            leader_assigned_to=leader)
        
        
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
        
        cancelled_requests = cex_requests.filter(state='cancelled').count(
        ) + monitoring_requests.filter(state='cancelled').count(
        ) + pos_requests.filter(state='cancelled').count(
        )
        
        
        data.append([(leader.first_name + ' ' + leader.last_name), approved_requests,
                    review_requests, for_validate_requests,cancelled_requests])
        
        
        best_to_worse_leader.append([(leader.first_name + ' ' + leader.last_name), quality_calculator(approved_requests, review_requests, for_validate_requests,cancelled_requests)])

    best_to_worse_leader = sorted(best_to_worse_leader, key=lambda x: x[1], reverse=True)

    best_to_worse_leader = best_to_worse_leader[:5]

    best_to_worse_leader_with_percentage = [(nombre, f"{porcentaje} %") for nombre, porcentaje in best_to_worse_leader]

    
    
    return {
        'leader_data': data,
        'leader_quality': best_to_worse_leader_with_percentage,
    }


def quality_calculator(approved_requests, under_review_requests, for_validate_requests, cancelled_requests):
    total = approved_requests + under_review_requests + for_validate_requests + cancelled_requests

    if total != 0:
        quality = ((approved_requests + cancelled_requests)/ total) * 100
        quality = round(quality, 2)
        return quality
    else:
        return 0 

def get_average_duration():
    approved_or_cancelled_requests = (
        list(CEXContractRequest.objects.filter(Q(state='filed') | Q(state='cancelled'))) +
        list(MonitoringContractRequest.objects.filter(Q(state='filed') | Q(state='cancelled'))) +
        list(ProvisionOfServicesContractRequest.objects.filter(Q(state='filed') | Q(state='cancelled')))
    )
    
    total_duration_seconds = sum((request.completion_date - timezone.make_aware(datetime.combine(request.start_date, datetime.min.time()), timezone.utc)).total_seconds() for request in approved_or_cancelled_requests if request.completion_date and request.start_date)
    total_count = len(approved_or_cancelled_requests)
    total_avg_duration_seconds = total_duration_seconds / total_count if total_count > 0 else 0

    total_days, remainder = divmod(total_avg_duration_seconds, 86400)
    total_hours, remainder = divmod(remainder, 3600)
    total_minutes, _ = divmod(remainder, 60)

    return {
        'average_days': int(total_days),
        'average_hours': int(total_hours),
        'average_minutes': int(total_minutes)
    }
    
def get_resolved_after_estimated_date():
    approved_or_cancelled_requests = (
        list(CEXContractRequest.objects.filter(Q(state='filed') | Q(state='cancelled'))) +
        list(MonitoringContractRequest.objects.filter(Q(state='filed') | Q(state='cancelled'))) +
        list(ProvisionOfServicesContractRequest.objects.filter(Q(state='filed') | Q(state='cancelled')))
    )

    resolved_after_estimated_date_count = 0

    for request in approved_or_cancelled_requests:
        if request.estimated_completion_date and request.completion_date:
            estimated_completion_date_datetime = datetime.combine(request.estimated_completion_date, datetime.min.time())
            estimated_completion_date_datetime_aware = timezone.make_aware(estimated_completion_date_datetime)
            if request.completion_date > estimated_completion_date_datetime_aware:
                resolved_after_estimated_date_count += 1

    return resolved_after_estimated_date_count





