from django.shortcuts import redirect
from django.views import View
from .utilities import utilities
from hiring_app.model.user_model import CustomUser

class AssignLeaderView(View):

    def post(self, request, idContract):
        user = self.request.user
        is_admin = any(group.name == 'admin' for group in user.groups.all())
        if is_admin:
            contract_request = utilities.getContract(idContract)
            new_leader_id = request.POST.get('leader')
            leaders = utilities.getGroupUsers('leader')
            new_leader = CustomUser.objects.filter(pk=new_leader_id).first()

            if new_leader in leaders:
                contract_request.leader_assigned_to = new_leader
                contract_request.save()
            else:
                request.session['error_message'] = 'Selected user is not leader.'
        else:
            request.session['error_message'] = 'You do not have permission for this action.'
        return redirect(request.META.get('HTTP_REFERER'))

