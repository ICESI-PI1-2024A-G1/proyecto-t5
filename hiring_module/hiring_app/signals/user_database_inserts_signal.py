from hiring_app.model.user_model import CustomUser
from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps
from django.conf import settings
import json
import os

DEFAULT_GROUPS = ['admin', 'leader', 'manager']

default_users_path = os.path.join(settings.BASE_DIR, 'hiring_app','intial_data', 'users.json')

DEFAULT_USERS = json.load(open(default_users_path))

def create_default_groups():
    for group_name in DEFAULT_GROUPS:
        if not Group.objects.filter(name=group_name).exists():
            Group.objects.create(name=group_name)

@receiver(post_migrate)
def user_database_inserts_signal(sender, **kwargs):
    auth_config = apps.get_app_config('auth')
    if sender != auth_config:
        return
    create_default_groups()
    for user_data in DEFAULT_USERS:
        user_id = user_data['id']
        if not CustomUser.objects.filter(id=user_id).exists():
            user = CustomUser.objects.create_user(
                id=user_data['id'],
                email=user_data['email'],
                password=user_data['password'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                birth_date=user_data['birth_date'],
                gender=user_data['gender'],
                address=user_data['address'],
                is_superuser=user_data.get('is_superuser', False),
                is_staff=user_data.get('is_staff', False)
            )
            if 'groups' in user_data:
                group_name = user_data['groups']
                if group_name:
                    group = Group.objects.get(name=group_name)
                    user.groups.add(group)