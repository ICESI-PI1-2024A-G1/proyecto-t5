from django.urls import include, path
from hiring_app.views import *

app_name = 'hiring_app'

urlpatterns = [
    path('external_user_dashboard/', ExternalUserDashboardView.as_view(), name = 'external_user_dashboard'),
    path('administrator_dashboard/', AdministratorDashboardView.as_view(), name = 'administrator_dashboard'),
    path('leader_dashboard/', LeaderDashboardView.as_view(), name = 'leader_dashboard'),
    path('manager_dashboard/', ManagerDashboardView.as_view(), name = 'manager_dashboard'),
    path('info/<str:idContract>/', ChangeState.as_view(), name='multiply_by_two'),
    path('request_creation/cex', CEXContractRequestView.as_view(), name = 'cex',),
    path('request_creation/monitoring', MonitoringContractRequestView.as_view(), name = 'monitoring',),

]