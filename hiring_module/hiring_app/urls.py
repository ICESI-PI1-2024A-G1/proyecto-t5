from django.urls import include, path
<<<<<<< HEAD
from hiring_app.views import ExternalUserDashboardView, AdministratorDashboardView, LeaderDashboardView, ManagerDashboardView, InfoView
=======
from hiring_app.views import *
>>>>>>> e23257135934b5973cbac37afe1f0fa65fbe0a23

app_name = 'hiring_app'

urlpatterns = [
    path('external_user_dashboard/', ExternalUserDashboardView.as_view(), name = 'external_user_dashboard'),
    path('administrator_dashboard/', AdministratorDashboardView.as_view(), name = 'administrator_dashboard'),
    path('leader_dashboard/', LeaderDashboardView.as_view(), name = 'leader_dashboard'),
    path('manager_dashboard/', ManagerDashboardView.as_view(), name = 'manager_dashboard'),
<<<<<<< HEAD
    path('info/<str:idContract>/', InfoView.as_view(), name='multiply_by_two'),
=======
    path('info/<str:idContract>/', ChangeState.as_view(), name='multiply_by_two'),
    path('request_creation/cex', CEXContractRequestView.as_view(), name = 'cex',),
    path('request_creation/monitoring', MonitoringContractRequestView.as_view(), name = 'monitoring',),

>>>>>>> e23257135934b5973cbac37afe1f0fa65fbe0a23
]