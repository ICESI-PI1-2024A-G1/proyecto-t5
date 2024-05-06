from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from hiring_app.model import CustomUser
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth.models import Group

class utilities:
    # Send email to user when request is created
    def send_email(subject, content, recipient):
        msg = MIMEMultipart()
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(content, 'html'))

        with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.login(settings.EMAIL_HOST_USER,
                        settings.EMAIL_HOST_PASSWORD)
            server.send_message(msg)

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
            )) + Count('leader_provisionofservicescontractrequest_requests', filter=(
                Q(leader_provisionofservicescontractrequest_requests__state='pending') |
                Q(leader_provisionofservicescontractrequest_requests__state='review') |
                Q(leader_provisionofservicescontractrequest_requests__state='incomplete')
            ))
        ).order_by('num_contracts', 'last_name')
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
            )) + Count('manager_provisionofservicescontractrequest_requests', filter=(
                Q(manager_provisionofservicescontractrequest_requests__state='pending') |
                Q(manager_provisionofservicescontractrequest_requests__state='review') |
                Q(manager_provisionofservicescontractrequest_requests__state='incomplete')
            ))
        ).order_by('num_contracts', 'last_name')
        return managers_with_least_contracts.first()
