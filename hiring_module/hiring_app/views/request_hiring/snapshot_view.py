from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render
from django.views import View
from hiring_app.views.request_hiring.utilities import utilities
from hiring_app.model.contract_request_model import state_choices
from django.contrib.auth.models import Group
from hiring_app.model.user_model import CustomUser
from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.contract_request_snapshot_model import ContractRequestSnapshot
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Description: View for handling snapshots of contract requests.
# Input: HTTP GET or POST request, idContract (int): The ID of the contract request.
# Output: Renders the snapshots_list.html template with relevant data (POST), or redirects the user based on their role (GET).
class SnapshotsView(View):

    # Description: Handles the GET request for viewing snapshots of contract requests.
    # Input: HTTP GET request, idContract (int): The ID of the contract request.
    # Output: Redirects the user based on their role.
    def get(self, request, idContract):
        is_admin = any(group.name == 'admin' for group in self.request.user.groups.all())
        is_leader = any(group.name == 'leader' for group in self.request.user.groups.all())
        is_manager = any(group.name == 'manager' for group in self.request.user.groups.all())

        if not (is_admin or is_leader or is_manager):
            return HttpResponseRedirect(reverse_lazy('hiring_app:external_user_dashboard'))

    # Description: Handles the POST request for viewing snapshots of contract requests or editing comments.
    # Input: HTTP POST request, idContract (int): The ID of the contract request.
    # Output: Renders the snapshots_list.html template with relevant data (if action is 'view-snapshots'), or edits the comment of the contract request (if action is 'edit-comment').
    def post(self, request, idContract):
        action = request.POST.get('action')
        if action == 'view-snapshots':
            contract_request = utilities.getContract(idContract)
            snapshots = contract_request.get_snapshots()
            return render(request, 'request_hiring/snapshots_list.html', {'snapshots': snapshots})
        
        if action == 'edit-comment':
            contract_request = utilities.getContract(idContract)
            comment = request.POST.get('comment')
            contract_request.edit_comment(comment)
            return HttpResponse('Comment edited successfully')
            
