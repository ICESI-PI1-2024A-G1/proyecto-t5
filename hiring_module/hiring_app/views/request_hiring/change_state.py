from django.shortcuts import redirect
from django.views import View
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .utilities import utilities
from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest
from hiring_app.model.contract_request_snapshot_model import ContractRequestSnapshot
from hiring_app.model.user_model import CustomUser
from django.urls import reverse
from django.http import HttpResponseRedirect

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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


class ChangeStateView(View):
    def post(self, request, idContract):
        contract_request = utilities.getContract(idContract)
        new_state = request.POST.get('state')
        reason = request.POST.get('reason')
        print(new_state)
        print(reason)
        state_actions = {
            'incomplete': {
                'email_function': self.send_email_file
            },
            'cancelled': {
                'email_function': self.send_email_request
            },
            'filed': {
                'email_function': self.send_email_success
            }
        }
        if not contract_request.is_valid_transition(new_state):
            request.session['error_message'] = "Esta opción no es válida"
            return HttpResponseRedirect(reverse('hiring_app:info', kwargs={'idContract': idContract}))

        if state_actions.get(new_state):
            state_actions.get(new_state)['email_function'](contract_request, reason)
            
        contract_request.transition_to_state(new_state)

        return HttpResponseRedirect(reverse('hiring_app:info', kwargs={'idContract': idContract}))

    def send_email_request(self, contract_request, reason):
        content = f"Estimado/a {contract_request.created_by.first_name},\n\nLamentamos informarle que su solicitud ha sido cancelada. El motivo proporcionado es: {reason}.\n\nPor favor, no dude en ponerse en contacto con nosotros si tiene alguna pregunta.\n\nAtentamente,\nTu aplicación"
        send_email('Solicitud cancelada', content,
                   "alejandrolonber25@gmail.com")

    def send_email_file(self, contract_request, reason):
        content = f"Estimado/a {contract_request.created_by.first_name},\n\nLe informamos que hemos identificado documentos faltantes en su solicitud. El motivo proporcionado es: {reason}.\n\nPor favor, proporcione la documentación faltante lo antes posible para continuar con el proceso.\n\nSi tiene alguna pregunta o necesita ayuda, no dude en ponerse en contacto con nosotros.\n\nAtentamente,\nTu aplicación"
        send_email('Solicitud de documentación faltante',
                   content, "alejandrolonber25@gmail.com")

    def send_email_success(self, contract_request, reason=""):
        content = f"Estimado/a {contract_request.created_by.first_name},\n\nNos complace informarle que su solicitud ha sido completada exitosamente.\n\nPor favor, no dude en ponerse en contacto con nosotros si tiene alguna pregunta o necesita asistencia adicional.\n\nAtentamente,\nTu aplicación"
        send_email('Solicitud completada exitosamente',
                   content, "alejandrolonber25@gmail.com")
