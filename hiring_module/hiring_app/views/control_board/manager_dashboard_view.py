from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from hiring_app.views.control_board.utilities import role_redirect, get_requests

class ManagerDashboardView(View):
    template_name = 'control_board/manager_dashboard.html'

    # Redirect to correct dashboard based on user role
    @method_decorator(role_redirect)
    def dispatch(self, request, *args, **kwargs):
        context = {}
        context.update(get_requests(self.request.user))
        return render(request, self.template_name, context)
    
    

    
    
