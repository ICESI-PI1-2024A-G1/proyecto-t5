from django.conf import settings
from django.core.mail import EmailMultiAlternatives

class utilities:
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
