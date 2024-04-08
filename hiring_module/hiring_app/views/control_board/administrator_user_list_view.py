from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.db.models import Q, CharField, Value
from django.db.models.functions import Concat

from hiring_app.model.user_model import CustomUser
from .utilities import admin_required



class AdministratorUserListView(TemplateView):
    template_name = 'administrator_user_list.html'

    # Redirect to correct dashboard based on user role
    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = CustomUser.objects.filter(groups__name__in=['admin', 'leader', 'manager'])
        # Add a role field to each user object
        for user in users:
            user.role = str(user.groups.first())
        context['users'] = users
        return context
    
    def post(self, request, *args, **kwargs):
        search_query = request.POST.get('search_query')
        if 'clear_search' in request.POST:
            search_query = None

        if 'search_by' in request.POST:
            # If either search button is clicked, determine which type of search is requested
            search_by = request.POST.get('search_by')
            if search_by == 'email':
                users = CustomUser.objects.filter(email__icontains=search_query, groups__name__in=['admin', 'leader', 'manager'])
            elif search_by == 'name':
                search_terms = search_query.split()
                query = Q()
                for term in search_terms:
                    query &= (Q(first_name__icontains=term) | Q(last_name__icontains=term))
                    # Filter users based on the query
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

