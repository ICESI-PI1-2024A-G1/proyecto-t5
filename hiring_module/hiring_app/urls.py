from django.urls import include, path
from hiring_app.views import *

app_name = 'hiring_app'

urlpatterns = [
    path('control_board/', ControlBoardView.as_view(), name = 'control_board',),
    path('info/<str:idContract>/', ChangeState.as_view(), name='multiply_by_two'),
    path('request_creation/cex', CEXContractRequestView.as_view(), name = 'cex',),
    path('request_creation/monitoring', MonitoringContractRequestView.as_view(), name = 'monitoring',),

]