from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from ..utilities import leader_or_admin_redirect_to_manager_statistics, get_metrics, get_average_duration

# Description: View class for the manager statistics page.
# Input: View (Class): Django class-based view.
# Output: None
class StatisticsView(View):
    template_name = 'statistical_registers/manager_statistics.html'

    # Description: Renders the manager statistics page.
    # Input: request (HttpRequest): The request object.
    # Output: Rendered HTML template displaying manager statistics.
    def dispatch(self, request, *args, **kwargs):
        metrics = get_metrics()
        average_duration = get_average_duration()
        metrics['average_duration'] = average_duration
        if self.request.user.groups.first().name == 'admin':
            metrics['actualgroup'] = 'admin'
        return render(request, self.template_name, metrics)
