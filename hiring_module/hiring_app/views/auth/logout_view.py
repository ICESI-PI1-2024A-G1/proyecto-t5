from django.contrib.auth.views import LogoutView

class LogoutView(LogoutView):
    next_page = 'login'
