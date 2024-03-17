from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from hiring_app.models import *

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

class ContractRequestModelTests(TestCase):
    def test_create_contract_request(self):
        # Create a user
        User = get_user_model()
        user = User.objects.create_user(id=1, password='1', first_name='John', last_name='Doe', birth_date='1990-01-01', gender='Male', address='1234 Main St')
        # Create a contract request
        contract_request = ContractRequest.objects.create_contract_request(created_by=user, estimated_completion_date='2024-10-10')
        self.assertEqual(contract_request.created_by, user)
        self.assertEqual(contract_request.state, 'pending')
        # Assign a user to the contract request
        # Create a new user
        assigned_to = User.objects.create_user(id=2, password='2', first_name='Jane', last_name='Doe', birth_date='1990-01-01', gender='Female', address='1234 Main St')
        contract_request.assign_to(user=assigned_to)
        self.assertEqual(contract_request.assigned_to, assigned_to)
        # Try to create a contract request without a creator
        with self.assertRaises(TypeError):
            ContractRequest.objects.create_contract_request()
        # Try to create a contract request with wrong user input
        with self.assertRaises(ValueError):
            ContractRequest.objects.create_contract_request(created_by=1)
        # Try to assign a wrong user
        with self.assertRaises(ValueError):
            contract_request.assign_to(user=1)
        
    def test_transition_to_state(self):
        # Create a user
        User = get_user_model()
        user = User.objects.create_user(id=1, password='1', first_name='John', last_name='Doe', birth_date='1990-01-01', gender='Male', address='1234 Main St')
        # Create a contract request
        contract_request = ContractRequest.objects.create_contract_request(created_by=user, estimated_completion_date='2024-10-10')
        # Transition to a new state
        contract_request.transition_to_state(new_state='review', comment='review state')
        self.assertEqual(contract_request.state, 'review')
        self.assertEqual(contract_request.comment, 'review state')
        # Check if the snapshot was created
        self.assertEqual(contract_request.get_snapshots().count(), 1)
        # Transition to a new state with comment
        contract_request.transition_to_state(new_state='filed', comment='filed state')
        self.assertEqual(contract_request.state, 'filed')
        self.assertEqual(contract_request.comment, 'filed state')
        # Check if the snapshot was created and has the comment of the previous state
        self.assertEqual(contract_request.get_snapshots().count(), 2)
        self.assertEqual(contract_request.get_snapshots().filter(state='review').first().comment, 'review state')
        # Try to transition to a non existent state
        with self.assertRaises(ValueError):
            contract_request.transition_to_state(new_state='foo')
        # Try to transition to a state previously transitioned to
        with self.assertRaises(ValueError):
            contract_request.transition_to_state(new_state='review')
