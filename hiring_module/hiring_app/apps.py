from django.apps import AppConfig


class Hiring_apppConfig(AppConfig):    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hiring_app'

    def ready(self):
        from hiring_app.signals import user_database_inserts_signal