from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from hiring_app.model import CustomUser
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth.models import Group

class utilities:
    # Send email to user when request is created
    def sendEmailSuccess(created_by):
            content = f'Estimado/a {created_by.first_name},\n\nNos complace informarle que su solicitud ha sido creada exitosamente.\n\nPor favor, no dude en ponerse en contacto con nosotros para contestar sus dudas.'

            message = EmailMultiAlternatives(
                'Solicitud creada',
                content,
                settings.EMAIL_HOST_USER,
                [created_by.email]
            )

            message.attach_alternative(content, 'text/html')
            message.send()

    def findLeaderToAssign():
        #Find the leader with the least ammount of active requests
        group = Group.objects.get(name="leader")
        leaders_with_least_contracts = CustomUser.objects.filter(groups=group).annotate(
            num_contracts=Count('leader_monitoringcontractrequest_requests', filter=(
                Q(leader_monitoringcontractrequest_requests__state='pending') |
                Q(leader_monitoringcontractrequest_requests__state='review') |
                Q(leader_monitoringcontractrequest_requests__state='incomplete')
            )) + Count('leader_cexcontractrequest_requests', filter=(
                Q(leader_cexcontractrequest_requests__state='pending') |
                Q(leader_cexcontractrequest_requests__state='review') |
                Q(leader_cexcontractrequest_requests__state='incomplete')
            ))
        ).order_by('-num_contracts', 'last_name')
        return leaders_with_least_contracts.first()
    
    def findManagerToAssign():
        #Find the manager with the least ammount of active requests
        group = Group.objects.get(name="manager")
        managers_with_least_contracts = CustomUser.objects.filter(groups=group).annotate(
            num_contracts=Count('manager_monitoringcontractrequest_requests', filter=(
                Q(manager_monitoringcontractrequest_requests__state='pending') |
                Q(manager_monitoringcontractrequest_requests__state='review') |
                Q(manager_monitoringcontractrequest_requests__state='incomplete')
            )) + Count('manager_cexcontractrequest_requests', filter=(
                Q(manager_cexcontractrequest_requests__state='pending') |
                Q(manager_cexcontractrequest_requests__state='review') |
                Q(manager_cexcontractrequest_requests__state='incomplete')
            ))
        ).order_by('-num_contracts', 'last_name')
        return managers_with_least_contracts.first()
