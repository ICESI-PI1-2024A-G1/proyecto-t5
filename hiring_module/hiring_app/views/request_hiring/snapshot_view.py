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

class SnapshotsView(View):
    def post(self, request, idContract):
        action = request.POST.get('action')
        if action == 'view-snapshots':
            contract_request = utilities.getContract(idContract)
            snapshots = contract_request.get_snapshots()
            return render(request, 'snapshots_list.html', {'snapshots': snapshots})
        
        if action == 'edit-comment':
            contract_request = utilities.getContract(idContract)
            comment = request.POST.get('comment')
            snapshots = contract_request.get_snapshots()
            snapshot = snapshots.filter(state=contract_request.state).first()
            snapshot.comment = comment
            snapshot.save()
            return HttpResponse('Comment edited successfully')
        
        if action == 'view-snapshot':
            snapshot_id = request.POST.get('snapshot_id')
            snapshot = ContractRequestSnapshot.objects.get(id=snapshot_id)
            return render(request, 'snapshot_information.html', {'snapshot': snapshot})
    
