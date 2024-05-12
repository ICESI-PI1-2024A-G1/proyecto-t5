from django.shortcuts import redirect
from django.views import View
from hiring_app.model.user_model import CustomUser
from .utilities import export_requests
class ExportRequestsView(View):

    def get(self, request):
        return export_requests(self.request.user)