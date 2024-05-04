from django.shortcuts import redirect, render
from django.views import View
from .utilities import utilities
from hiring_app.model.user_model import CustomUser

# Description: View for assigning a leader to a contract request.
# Input: None
# Output: None
class AssignManagerView(View):

    # Description: Handles the assignment of a manager to a contract request.
    # Input: HTTP POST request, idContract (int): The ID of the contract request.
    # Output: Redirects to the referring page after processing the request.
    def post(self, request, idContract):
        user = self.request.user
        
        is_leader_or_admin = any(group.name in ['leader', 'admin'] for group in user.groups.all())     
        if is_leader_or_admin:
            contract_request = utilities.getContract(idContract)
            new_manager_id = request.POST.get('manager')
            managers = utilities.getGroupUsers('manager')
            new_manager = CustomUser.objects.filter(pk=new_manager_id).first()
        
            if new_manager in managers:
                contract_request.manager_assigned_to = new_manager
                contract_request.save()
            else:
                request.session['error_message'] = 'Selected user is not manager.'
        else:
            request.session['error_message'] = 'You do not have permission for this action.'
        return redirect(request.META.get('HTTP_REFERER'))

