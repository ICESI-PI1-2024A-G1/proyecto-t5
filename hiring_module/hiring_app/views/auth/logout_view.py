from django.contrib.auth.views import LogoutView

class LogoutView(LogoutView):
    # Redirect to login page after logout
    next_page = 'login'
