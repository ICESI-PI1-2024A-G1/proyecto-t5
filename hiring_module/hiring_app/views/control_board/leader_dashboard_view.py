from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from hiring_app.views.control_board.utilities import role_redirect, get_requests

# Description: View for displaying the leader dashboard.
# Input: View
# Output: Renders the leader dashboard template.
class LeaderDashboardView(View):
    template_name = 'control_board/leader_dashboard.html'

    # Description: Dispatch method to redirect based on user role.
    # Input: self, request, *args, **kwargs
    # Output: Renders the leader dashboard template with context.
    @method_decorator(role_redirect)
    def dispatch(self, request, *args, **kwargs):
        context = {
            'actualgroup': 'leader'
        }
        context.update(get_requests(self.request.user))
        return render(request, self.template_name, context)
    
    