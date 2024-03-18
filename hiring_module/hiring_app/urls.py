from django.urls import include, path
from hiring_app.views import ControlBoardView

app_name = 'hiring_app'

urlpatterns = [
    path('control_board/', ControlBoardView.as_view(), name = 'control_board',)

]