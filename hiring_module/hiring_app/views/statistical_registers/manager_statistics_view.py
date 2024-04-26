from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from .utilities import leader_redirect_to_manager_statistics  # Importar el decorador



class ManagerStatisticsView(View):
    template_name = 'statistical_registers/manager_statistics.html'
    
    @method_decorator(leader_redirect_to_manager_statistics)
    def dispatch(self, request, *args, **kwargs):
        # Aquí puedes agregar cualquier lógica adicional que necesites antes de mostrar la vista
        return render(request, self.template_name)