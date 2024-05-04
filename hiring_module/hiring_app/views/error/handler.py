from django.shortcuts import render
from django.views import View


class ErrorHandlerView(View):
    def get(self, request, exception=None, error_code=None):
        error_title = "Error"
        error_description = "Oops! Something went wrong."

        if error_code == 404:
            error_title = "404"
            error_description = "It looks like you found a glitch in the matrix..."

        return render(request, 'error/general.html', {
            'error_title': error_title,
            'error_description': error_description
        })
