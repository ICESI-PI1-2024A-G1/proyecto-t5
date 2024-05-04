from functools import wraps
from django.shortcuts import redirect

from hiring_app.model import CustomUser
from django.contrib.auth.models import Group

from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest
from hiring_app.model.provision_of_services_request_model import ProvisionOfServicesContractRequest

# Description: Decorator to redirect users to the correct dashboard based on their role.
# Input: view_func (function): The view function to be wrapped.
# Output: wrapper function: Redirects users to the appropriate dashboard based on their role.
def role_redirect(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name='admin').exists() and request.path != '/hiring_app/administrator_dashboard/':
            return redirect('hiring_app:administrator_dashboard')
        elif request.user.groups.filter(name='leader').exists() and request.path != '/hiring_app/leader_dashboard/':
            return redirect('hiring_app:leader_dashboard')
        elif request.user.groups.filter(name='manager').exists() and request.path != '/hiring_app/manager_dashboard/':
            return redirect('hiring_app:manager_dashboard')
        elif not request.user.groups.exists() and request.path != '/hiring_app/external_user_dashboard/':
            return redirect('hiring_app:external_user_dashboard')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper

# Description: Decorator to ensure that only users with the 'admin' role can access a view.
# Input: view_func (function): The view function to be wrapped.
# Output: wrapper function: Redirects non-admin users to appropriate dashboards.
def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.groups.filter(name='admin').exists():
            if request.user.groups.filter(name='leader').exists():
                return redirect('hiring_app:leader_dashboard')
            elif request.user.groups.filter(name='manager').exists():
                return redirect('hiring_app:manager_dashboard')
            else:
                return redirect('hiring_app:external_user_dashboard')
        return view_func(request, *args, **kwargs)
    
    return wrapper

# Description: Decorator to ensure that only users with the 'leader' role can access a view.
# Input: view_func (function): The view function to be wrapped.
# Output: wrapper function: Redirects non-leader users to appropriate dashboards.
def leader_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.groups.filter(name='leader').exists():
            if request.user.groups.filter(name='admin').exists():
                return redirect('hiring_app:administrator_dashboard')
            elif request.user.groups.filter(name='manager').exists():
                return redirect('hiring_app:manager_dashboard')
            else:
                return redirect('hiring_app:external_user_dashboard')
        return view_func(request, *args, **kwargs)
    
    return wrapper

# Description: Decorator to ensure that only users with the 'manager' role can access a view.
# Input: view_func (function): The view function to be wrapped.
# Output: wrapper function: Redirects non-manager users to appropriate dashboards.
def manager_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.groups.filter(name='manager').exists():
            if request.user.groups.filter(name='admin').exists():
                return redirect('hiring_app:administrator_dashboard')
            elif request.user.groups.filter(name='leader').exists():
                return redirect('hiring_app:leader_dashboard')
            else:
                return redirect('hiring_app:external_user_dashboard')
        return view_func(request, *args, **kwargs)
    
    return wrapper

# Description: Retrieve various types of contract requests based on user's role.
# Input: user (CustomUser): The user for whom to retrieve requests.
# Output: Dictionary: Contains different types of contract requests and related information.
def get_requests(user):
    groups = [group.name for group in user.groups.all()]
    requests_CEX = CEXContractRequest.objects.none()
    requests_monitoring = MonitoringContractRequest.objects.none()
    requests_pos = ProvisionOfServicesContractRequest.objects.none()

    if 'admin' in groups:
        requests_CEX = CEXContractRequest.objects.all()
        requests_monitoring = MonitoringContractRequest.objects.all()
        requests_pos = ProvisionOfServicesContractRequest.objects.all()
    elif 'leader' in groups:
        requests_CEX = CEXContractRequest.objects.filter(leader_assigned_to=user.id)
        requests_monitoring = MonitoringContractRequest.objects.filter(leader_assigned_to=user.id)
        requests_pos = ProvisionOfServicesContractRequest.objects.filter(leader_assigned_to=user.id)
    elif 'manager' in groups:
        requests_CEX = CEXContractRequest.objects.filter(manager_assigned_to=user.id)
        requests_monitoring = MonitoringContractRequest.objects.filter(manager_assigned_to=user.id)
        requests_pos = ProvisionOfServicesContractRequest.objects.filter(manager_assigned_to=user.id)
          
    groupManager = Group.objects.get(name='manager')
    groupLeader = Group.objects.get(name='leader')       
    managers = list(CustomUser.objects.filter(groups=groupManager))
    leaders = list(CustomUser.objects.filter(groups=groupLeader))
    return {
        'requests': list(requests_CEX) + list(requests_monitoring) + list(requests_pos),
        'filled_requests': list(requests_CEX.filter(state='filed')) + list(requests_monitoring.filter(state='filed')) + list(requests_pos.filter(state='filed')),
        'reviewed_requests': list(requests_CEX.filter(state='review')) + list(requests_monitoring.filter(state='review')) + list(requests_pos.filter(state='review')),
        'for_validate_requests':  list(requests_CEX.filter(state__in=['pending', 'incomplete'])) + list(requests_monitoring.filter(state__in=['pending', 'incomplete'])) + list(requests_pos.filter(state__in=['pending', 'incomplete'])),
        'leaders': leaders,
        'managers': managers,
    }