from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse
from hiring_app.model import CustomUser
from django.contrib.auth.models import Group
from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest

# Decorador para redirigir a los líderes a la página de estadísticas del manager


# Decorador para redirigir a los líderes y administradores a la página de estadísticas del manager
def leader_or_admin_redirect_to_manager_statistics(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Si el usuario no está autenticado, redirigirlo al inicio de sesión
            return redirect('login')

        if request.user.groups.filter(name__in=['leader', 'admin']).exists():
            # Si el usuario es líder o administrador, y no está en la página de estadísticas del manager, redirigirlo allí
            if not request.path == reverse('hiring_app:manager_statistics'):
                return redirect('hiring_app:manager_statistics')

        # Si no es líder ni administrador, o ya está en la página de estadísticas del manager, llamar a la vista original
        return view_func(request, *args, **kwargs)

    return wrapper


def get_metrics(user):
    # Obtener todos los gestores
    group_manager = Group.objects.get(name='manager')
    managers = CustomUser.objects.filter(groups=group_manager)

    # Inicializar el contador de solicitudes
    total_requests = 0
    approved_requests = 0
    review_requests = 0
    for_validate_requests = 0
    best_manager = None
    max_approved_requests = 0
    all_requests_assigned_to_the_best_manager = 0

    # Contar las solicitudes asignadas a cada gestor
    for manager in managers:
        # Consultar las solicitudes asignadas a este gestor en CEXContractRequest
        cex_requests = CEXContractRequest.objects.filter(
            manager_assigned_to=manager)
        # Consultar las solicitudes asignadas a este gestor en MonitoringContractRequest
        monitoring_requests = MonitoringContractRequest.objects.filter(
            manager_assigned_to=manager)

        # Combinar los resultados de ambas consultas
        total_requests_for_a_manager = cex_requests.count() + monitoring_requests.count()
        approved_requests += cex_requests.filter(state='filed').count(
        ) + monitoring_requests.filter(state='filed').count()
        review_requests += cex_requests.filter(state='review').count(
        ) + monitoring_requests.filter(state='review').count()
        for_validate_requests += cex_requests.filter(state__in=['pending', 'incomplete']).count(
        ) + monitoring_requests.filter(state__in=['pending', 'incomplete']).count()

        total_requests += total_requests_for_a_manager

        if approved_requests > max_approved_requests:
            max_approved_requests = approved_requests
            best_manager = manager.first_name + ' ' + manager.last_name
            all_requests_assigned_to_the_best_manager = total_requests_for_a_manager

    if best_manager:
        effectiveness_percentage = (
            max_approved_requests / all_requests_assigned_to_the_best_manager) * 100
    else:
        effectiveness_percentage = 0

    # Devolver las métricas
    return {
        'total_requests': total_requests,
        'approved_requests': approved_requests,
        'review_requests': review_requests,
        'for_validate_requests': for_validate_requests,
        'best_manager': best_manager,
        'effectiveness_percentage': effectiveness_percentage,
    }
