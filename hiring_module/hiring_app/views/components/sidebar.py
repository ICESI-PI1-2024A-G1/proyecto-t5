from django.shortcuts import redirect, render
from django.views import View
from hiring_app.model.user_model import CustomUser

class UserDetailView(DetailView):
    user = self.request.user

    model = CustomUser
    template_name = 'user_detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['groups'] = user.groups.all()
        return context
