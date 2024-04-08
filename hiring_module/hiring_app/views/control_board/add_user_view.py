from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import Group
from hiring_app.model.user_model import CustomUser
from hiring_app.views.control_board.utilities import admin_required
from django.utils.decorators import method_decorator
from django.db.models import Q, CharField, Value
from django.db.models.functions import Concat

class AddUserView(TemplateView):
    template_name = 'administrator_add_user.html'

    # Redirect to correct dashboard based on user role
    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # External users are users who are not admins, leaders, or managers
        users = CustomUser.objects.exclude(groups__name__in=['admin', 'leader', 'manager'])
        # Add a role field to each user object
        for user in users:
            user.role = str(user.groups.first())
        context['users'] = users
        return context
    
    def post(self, request, *args, **kwargs):            
        if 'search_query' in request.POST:
            search_query = request.POST.get('search_query')
            if 'clear_search' in request.POST:
                search_query = None

            if 'search_by' in request.POST:
                # If either search button is clicked, determine which type of search is requested
                search_by = request.POST.get('search_by')
                if search_by == 'email':
                    users = CustomUser.objects.exclude(groups__name__in=['admin', 'leader', 'manager']).filter(email__icontains=search_query)
                elif search_by == 'name':
                    search_terms = search_query.split()
                    query = Q()
                    for term in search_terms:
                        query &= (Q(first_name__icontains=term) | Q(last_name__icontains=term))
                        # Filter users based on the query
                    users = CustomUser.objects.annotate(
                        full_name=Concat('first_name', Value(' '), 'last_name', output_field=CharField())
                    ).filter(query).exclude(groups__name__in=['admin', 'leader', 'manager'])

            else:
                # If no search button is clicked, display all users
                users = CustomUser.objects.exclude(groups__name__in=['admin', 'leader', 'manager'])

            context = self.get_context_data()
            for user in users:
                user.role = str(user.groups.first())
            context['users'] = users
            context['users'] = users
            return self.render_to_response(context)
        else:
            # Handle POST request to modify user group
            user_id = request.POST.get('user_id')
            role = request.POST.get('role')
            user = CustomUser.objects.get(pk=user_id)
            # Modify user's group based on selected role
            if role == 'admin':
                user.groups.set([Group.objects.get(name='admin')])
            elif role == 'leader':
                user.groups.set([Group.objects.get(name='leader')])
            else:
                user.groups.set([Group.objects.get(name='manager')])

            # Redirect to a success page or any other page as needed
            return HttpResponseRedirect(reverse('hiring_app:administrator_user_list'))