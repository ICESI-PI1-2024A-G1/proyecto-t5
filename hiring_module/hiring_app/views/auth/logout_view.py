from django.contrib.auth.views import LogoutView

# Description: View for handling user logout.
# Input: LogoutView
# Output: None
class LogoutView(LogoutView):
    next_page = 'login'
