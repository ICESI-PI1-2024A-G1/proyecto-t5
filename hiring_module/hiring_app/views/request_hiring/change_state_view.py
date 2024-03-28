from django.shortcuts import redirect
from django.views import View
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from hiring_app.model import CEXContractRequest
from hiring_app.model import state_choices
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from hiring_app.model.monitoring_contract_request_model import MonitoringContractRequest


class ChangeState(View):
    def get(self, request, idContract):
        contract_request = self.getContract(idContract)

        return render(request, 'request_hiring.html', {'choices': state_choices(), 'result': contract_request.state, 'id': idContract})

    def post(self, request, idContract):
        contract_request = self.getContract(idContract)
        new_state = request.POST.get('state')

        state_actions = {
            'incomplete': {
                'error_message': 'Debe ingresar un motivo para los documentos faltantes.',
                'email_function': self.sendEmailFile
            },
            'cancelled': {
                'error_message': 'Debe ingresar un motivo para la cancelacion.',
                'email_function': self.sendEmailRequest
            },
            'filed': {
                'error_message': None,
                'email_function': self.sendEmailSuccess
            }
        }

        action = state_actions.get(new_state, None)

        if not action:
            return render(request, 'request_hiring.html', {'choices': state_choices(), 'result': contract_request.state, 'error_message': 'Invalid state transition. Unable to change state.', 'id': idContract})

        reason = request.POST.get('reason')
        if action and (not reason and action['error_message']):
            return render(request, 'request_hiring.html', {'choices': state_choices(), 'result': contract_request.state, 'error_message': action['error_message'], 'id': idContract})
        elif action:
            contract_request.state = new_state
            contract_request.save()
            if action['email_function']:
                action['email_function'](contract_request, reason)

        return self.get(request, idContract)

    def getContract(self, idContract):
        contract_request = CEXContractRequest.objects.filter(
            id=idContract).first()

        if not contract_request:
            contract_request = MonitoringContractRequest.objects.filter(
                id=idContract).first()

        if not contract_request:
            raise Http404("Contract request does not exist")
        return contract_request


    def sendEmailRequest(self, contract_request, reason):
        content = f'Estimado/a {contract_request.created_by.first_name},\n\nLamentamos informarle que su solicitud ha sido cancelada. El motivo proporcionado es: {reason}.\n\nPor favor, no dude en ponerse en contacto con nosotros si tiene alguna pregunta.\n\nAtentamente,\nTu aplicación'

        message = EmailMultiAlternatives('Solicitud cancelada',
                                        content,
                                        settings.EMAIL_HOST_USER,
                                        [contract_request.created_by.email])

        message.attach_alternative(content, 'text/html')
        message.send()


    def sendEmailFile(self, contract_request, reason):
        content = f'Estimado/a {contract_request.created_by.first_name},\n\nLamentamos informarle que su solicitud ha sido cancelada. El motivo proporcionado es: {reason}.\n\nPor favor, no dude en ponerse en contacto con nosotros si tiene alguna pregunta.\n\nAtentamente,\nTu aplicación'

        message = EmailMultiAlternatives('Solicitud cancelada',
                                        content,
                                        settings.EMAIL_HOST_USER,
                                        [contract_request.created_by.email])

        message.attach_alternative(content, 'text/html')
        message.send()



    def sendEmailSuccess(self, contract_request, reason=""):
        content = f'Estimado/a {contract_request.created_by.first_name},\n\nNos complace informarle que su solicitud ha sido completada exitosamente.\n\nPor favor, no dude en ponerse en contacto con nosotros si tiene alguna pregunta o necesita asistencia adicional.\n\nAtentamente,\nTu aplicación'

        message = EmailMultiAlternatives(
            'Solicitud completada exitosamente',
            content,
            settings.EMAIL_HOST_USER,
            [contract_request.created_by.email]
        )

        message.attach_alternative(content, 'text/html')
        message.send()
