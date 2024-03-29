from django.shortcuts import render
from django.views import View
from hiring_app.views.request_hiring.utilities import utilities
from hiring_app.model.contract_request_model import state_choices
from django.contrib.auth.models import Group
from hiring_app.model.user_model import CustomUser

class RequestHiringView(View):
    def get(self, request, idContract):

        
        group = Group.objects.get(name='manager')
        managers = list(CustomUser.objects.filter(groups=group))
        contract_request = utilities.getContract(idContract)
        return render(request, 'request_hiring.html', {'choices': state_choices(), 'contract_request': contract_request, 'managers': managers, 'error_message': request.session.pop('error_message', None), 'user': self.request.user})