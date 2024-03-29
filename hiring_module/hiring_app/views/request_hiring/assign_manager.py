from django.shortcuts import redirect, render
from django.views import View
from .utilities import utilities
from hiring_app.model.user_model import CustomUser

class AssignManagerView(View):

    def post(self, request, idContract):
        contract_request = utilities.getContract(idContract)
        new_manager_id = request.POST.get('manager')
        managers = utilities.getGroupUsers('manager')
        new_manager = CustomUser.objects.filter(pk=new_manager_id).first()
    
        if new_manager in managers:
            contract_request.manager_assigned_to = new_manager
            contract_request.assign_manager(new_manager)
        else:
            request.session['error_message'] = 'Selected user is not manager.'
        return redirect('hiring_app:info', idContract=idContract)

