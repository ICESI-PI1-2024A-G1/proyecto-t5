from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.db.models import Q, CharField, Value
from django.db.models.functions import Concat

from hiring_app.model.user_model import CustomUser
from .utilities import admin_required
from django.contrib.auth.models import Group

# Description: View for listing administrator users.
# Input: TemplateView
# Output: Renders the administrator user list template with context data.
class AdministratorUserListView(TemplateView):
    template_name = 'admin_user/administrator_user_list.html'

    # Description: Dispatch method to check admin permission.
    # Input: self, *args, **kwargs
    # Output: Super dispatch method if user has admin permission.
    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # Description: Get context data for rendering template.
    # Input: **kwargs
    # Output: Context data for rendering template.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = CustomUser.objects.filter(groups__name__in=['admin', 'leader', 'manager'])
        for user in users:
            user.role = str(user.groups.first())
        context['users'] = users
        context['actualgroup'] = 'admin'
        return context
    
    # Description: Handle post request for updating user role or searching users.
    # Input: request, *args, **kwargs
    # Output: Rendered template with updated context data or search results.
    def post(self, request, *args, **kwargs):
        if 'updateRole' in request.POST:
            user_id = request.POST.get('userId')
            new_role = request.POST.get('role')
            user = CustomUser.objects.get(pk=user_id)
            if(new_role == 'remove'):
                user.groups.clear()
            else:
                user.groups.clear()
                user.groups.add(Group.objects.get(name=new_role))
            user.save()

        search_query = request.POST.get('search_query')
        if 'clear_search' in request.POST:
            search_query = None

        if 'search_by' in request.POST:
            search_by = request.POST.get('search_by')
            if search_by == 'email':
                users = CustomUser.objects.filter(email__icontains=search_query, groups__name__in=['admin', 'leader', 'manager'])
            elif search_by == 'name':
                search_terms = search_query.split()
                query = Q()
                for term in search_terms:
                    query &= (Q(first_name__icontains=term) | Q(last_name__icontains=term))
                users = CustomUser.objects.annotate(
                    full_name=Concat('first_name', Value(' '), 'last_name', output_field=CharField())
                ).filter(query, groups__name__in=['admin', 'leader', 'manager'])

        
        else:
            users = CustomUser.objects.filter(groups__name__in=['admin', 'leader', 'manager'])

        context = self.get_context_data()
        for user in users:
            user.role = str(user.groups.first())
        context['users'] = users
        return self.render_to_response(context)

