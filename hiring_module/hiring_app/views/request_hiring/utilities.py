from django.http import Http404
from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest
from django.contrib.auth.models import Group
from hiring_app.model.user_model import CustomUser

class utilities:
    def getContract(idContract):
        contract_request = CEXContractRequest.objects.filter(
            id=idContract).first()

        if not contract_request:
            contract_request = MonitoringContractRequest.objects.filter(
                id=idContract).first()

        if not contract_request:
            raise Http404("Contract request does not exist")
        return contract_request
    
    def getGroupUsers(groupName):
        group = Group.objects.get(name=groupName)
        return CustomUser.objects.filter(groups=group)