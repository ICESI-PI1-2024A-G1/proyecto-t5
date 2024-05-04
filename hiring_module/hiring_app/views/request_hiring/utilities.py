from django.http import Http404
from hiring_app.model.cex_contract_request_model import CEXContractRequest
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest
from hiring_app.model.provision_of_services_request_model import ProvisionOfServicesContractRequest
from django.contrib.auth.models import Group
from hiring_app.model.user_model import CustomUser

# Description: Utility functions for handling contract requests and group users.
# Input: None
# Output: None
class utilities:
    
    # Description: Retrieves a contract request based on its ID.
    # Input: idContract (int): The ID of the contract request.
    # Output: CEXContractRequest, MonitoringContractRequest, or ProvisionOfServicesContractRequest instance.
    def getContract(idContract):
        contract_request = CEXContractRequest.objects.filter(
            id=idContract).first()

        if not contract_request:
            contract_request = MonitoringContractRequest.objects.filter(
                id=idContract).first()
            
        if not contract_request:
            contract_request = ProvisionOfServicesContractRequest.objects.filter(
                id=idContract).first()

        if not contract_request:
            raise Http404("Contract request does not exist")
        return contract_request
    
    # Description: Retrieves users belonging to a specified group.
    # Input: groupName (str): The name of the group.
    # Output: QuerySet of CustomUser instances belonging to the specified group.
    def getGroupUsers(groupName):
        group = Group.objects.get(name=groupName)
        return CustomUser.objects.filter(groups=group)