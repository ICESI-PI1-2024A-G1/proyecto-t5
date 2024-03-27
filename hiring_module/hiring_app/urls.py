from django.urls import include, path
from hiring_app.views import ControlBoardView, ChangeState

app_name = 'hiring_app'

urlpatterns = [
    path('control_board/', ControlBoardView.as_view(), name = 'control_board',),
    path('info/<int:number>/', ChangeState.as_view(), name='multiply_by_two'),
]