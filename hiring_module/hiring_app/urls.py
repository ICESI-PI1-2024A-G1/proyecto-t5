from django.urls import include, path
from hiring_app.views import *
from hiring_app.views.request_hiring.assign_manager import AssignManagerView
from hiring_app.views.request_hiring.request_hiring_view import RequestHiringView
from hiring_app.views.request_hiring.change_state import ChangeStateView

app_name = 'hiring_app'

urlpatterns = [
    path('external_user_dashboard/', ExternalUserDashboardView.as_view(), name = 'external_user_dashboard'),
    path('administrator_dashboard/', AdministratorDashboardView.as_view(), name = 'administrator_dashboard'),
    path('leader_dashboard/', LeaderDashboardView.as_view(), name = 'leader_dashboard'),
    path('manager_dashboard/', ManagerDashboardView.as_view(), name = 'manager_dashboard'),
    path('info/<str:idContract>/', RequestHiringView.as_view(), name='info'),
    path('info/change_state/<str:idContract>/', ChangeStateView.as_view(), name='change_state'),
    path('info/assign_manager/<str:idContract>/', AssignManagerView.as_view(), name='assign_manager'),
    path('request_creation/cex/', CEXContractRequestView.as_view(), name = 'cex',),
    path('request_creation/monitoring/', MonitoringContractRequestView.as_view(), name = 'monitoring',),
]