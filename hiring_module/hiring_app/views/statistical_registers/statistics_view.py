from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.urls import reverse
from ..utilities import leader_or_admin_redirect_to_manager_statistics, get_manager_metrics, get_leader_metrics, get_average_duration, filter_quantity_of_requests_by_date_range



class StatisticsView(View):
    template_name = 'statistical_registers/statistics.html'

    #@method_decorator(leader_or_admin_redirect_to_manager_statistics)
    def dispatch(self, request, *args, **kwargs):
        # Get the required metrics

        print(reverse('statistics'))
        manager_metrics = get_manager_metrics()
        leader_metrics = get_leader_metrics()
        average_duration = get_average_duration()
        group = {'actualgroup': 'other'}
        user_group = self.request.user.groups.first()
        if user_group:
            if user_group.name == 'admin':
                group = {'actualgroup': 'admin'}
        # if self.request.user.groups.first().name == 'admin':
        #     group = {'actualgroup': 'admin'}
        context = {
            'manager_metrics': manager_metrics,
            'leader_metrics': leader_metrics,
            'average_duration': average_duration,
            'statistics_url': reverse('statistics'),
            'group': group
        }
        
        # Pass metrics as context to template
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        total_requests_count = filter_quantity_of_requests_by_date_range(start_date, end_date)
        return JsonResponse(total_requests_count)
