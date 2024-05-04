from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from hiring_app.views.control_board.utilities import role_redirect

# Description: View for displaying the leader dashboard.
# Input: TemplateView
# Output: Renders the leader dashboard template.
class LeaderDashboardView(TemplateView):
    template_name = 'leader_dashboard.html'

    # Description: Dispatch method to redirect based on user role.
    # Input: self, *args, **kwargs
    # Output: Super dispatch method with redirection based on user role.
    @method_decorator(role_redirect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    