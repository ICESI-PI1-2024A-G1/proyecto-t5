from django.apps import AppConfig

# Description: Configuration class for the hiring_app Django app.
# Input: AppConfig (Class): Django class for application configuration.
# Output: None
class Hiring_apppConfig(AppConfig):    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hiring_app'

    # Description: Method called when the app is ready.
    # Input: Self (Object): The object instance.
    # Output: None
    def ready(self):
        # Import signals to make sure they are registered
        from hiring_app.signals import user_database_inserts_signal