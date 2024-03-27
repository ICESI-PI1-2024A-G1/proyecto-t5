from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        # Create a user and check if the fields are correct
        user = User.objects.create_user(id=1, password='1', first_name='John', last_name='Doe', birth_date='1990-01-01', gender='Male', address='1234 Main St')
        self.assertEqual(user.id, 1)
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.birth_date, '1990-01-01')
        self.assertEqual(user.gender, 'Male')
        self.assertEqual(user.address, '1234 Main St')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        # Try to create a user with the same id
        try:
            user = User.objects.create_user(id=1, password='1', first_name='John', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')
        except IntegrityError:
            pass
        # Try to create a user without the required fields
        with self.assertRaises(TypeError):
            User.objects.create_user()
        # Try to create a user without the required fields
        with self.assertRaises(TypeError):
            User.objects.create_user(id=1)
        # Try to create a user with a string id
        with self.assertRaises(ValueError):
            User.objects.create_user(id="foo", password="foo", first_name='John', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')

    def text_create_superuser(self):
        User = get_user_model()
        # Create a superuser and check if the fields are correct
        admin_user = User.objects.create_superuser(id=1, password='1', first_name='John', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')
        self.assertEqual(admin_user.id, 1)
        self.assertEqual(admin_user.first_name, 'John')
        self.assertEqual(admin_user.last_name, 'Doe')
        self.assertEqual(admin_user.birth_date, '1990-01-01')
        self.assertEqual(admin_user.address, '1234 Main St')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        # Try to create a superuser with the same id
        try:
            admin_user = User.objects.create_superuser(id=1, password='1', first_name='John', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')
        except IntegrityError:
            pass
        # Try to create a superuser without the required fields
        with self.assertRaises(TypeError):
            User.objects.create_superuser()
        # Try to create a superuser without the required fields
        with self.assertRaises(TypeError):
            User.objects.create_superuser(id=1)
        # Try to create a superuser with a string id
        with self.assertRaises(ValueError):
            User.objects.create_superuser(id="foo", password='foo', first_name='John', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')
