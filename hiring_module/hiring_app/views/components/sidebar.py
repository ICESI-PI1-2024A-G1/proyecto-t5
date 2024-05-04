from django.shortcuts import redirect, render
from django.views import View
from hiring_app.model.user_model import CustomUser

# Description: View for displaying user details.
# Input: DetailView, request
# Output: Rendered template or redirect
class UserDetailView(DetailView):
    user = self.request.user

    model = CustomUser
    template_name = 'user_detail.html'
    context_object_name = 'user'

    # Description: Get additional context data for user detail view.
    # Input: kwargs
    # Output: Context data dictionary
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['groups'] = user.groups.all()
        return context
