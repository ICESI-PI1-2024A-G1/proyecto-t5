from django.test import TestCase
from django.core.exceptions import ValidationError
from hiring_app.model import MonitoringContractRequest
from django.contrib.auth import get_user_model

class MonitoringContractRequestTests(TestCase):
    def test_create_monitoring_contract_request(self):
        User = get_user_model()
        # Create a user
        user = User.objects.create_user(id=1, password='1', first_name='John', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')
        # Create a monitoring contract request
        monitoring_contract_request = MonitoringContractRequest.objects.create_contract_request(
            estimated_completion_date='2021-12-31',
            cenco = 'cenco',
            has_money_in_cenco = True,
            cenco_manager = 'cenco manager',
            monitoring_type = 'academic',
            student_code = 'student code',
            student_full_name = 'student full name',
            student_id = 'student id',
            student_email = 'student@example.com',
            student_cellphone = '1234567890',
            daviplata = 'daviplata',
            course_or_proyect = 'course',
            monitoring_description = 'monitoring description',
            weekly_hours = 10,
            total_value_to_pay = 1000000,
            is_unique_payment = True,
            created_by=user
        )
        self.assertEqual(monitoring_contract_request.id, 1)
        self.assertEqual(monitoring_contract_request.cenco, 'cenco')
        self.assertEqual(monitoring_contract_request.has_money_in_cenco, True)
        self.assertEqual(monitoring_contract_request.cenco_manager, 'cenco manager')
        self.assertEqual(monitoring_contract_request.monitoring_type, 'academic')
        self.assertEqual(monitoring_contract_request.student_code, 'student code')
        self.assertEqual(monitoring_contract_request.student_full_name, 'student full name')
        self.assertEqual(monitoring_contract_request.student_id, 'student id')
        self.assertEqual(monitoring_contract_request.student_email, 'student@example.com')
        self.assertEqual(monitoring_contract_request.student_cellphone, '1234567890')
        self.assertEqual(monitoring_contract_request.daviplata, 'daviplata')
        self.assertEqual(monitoring_contract_request.course_or_proyect, 'course')
        self.assertEqual(monitoring_contract_request.monitoring_description, 'monitoring description')
        self.assertEqual(monitoring_contract_request.weekly_hours, 10)
        self.assertEqual(monitoring_contract_request.total_value_to_pay, 1000000)
        self.assertEqual(monitoring_contract_request.is_unique_payment, True)
        # Assign the user to the contract request
        monitoring_contract_request.assign_to(user)
        self.assertEqual(monitoring_contract_request.assigned_to, user)
        # Try to create a monitoring contract request without the required fields
        with self.assertRaises(ValidationError):
            monitoring_contract_request = MonitoringContractRequest.objects.create_contract_request()
        # Try to create a monitoring contract request with a wrong email
        with self.assertRaises(ValidationError):
            monitoring_contract_request = MonitoringContractRequest.objects.create_contract_request(
                estimated_completion_date='2021-12-31',
                assigned_to=user,
                cenco = 'cenco',
                has_money_in_cenco = True,
                cenco_manager = 'cenco manager',
                monitoring_type = 'academic',
                student_code = 'student code',
                student_full_name = 'student full name',
                student_id = 'student id',
                student_email = 'student',
                student_cellphone = '1234567890',
                daviplata = 'daviplata',
                course_or_proyect = 'course',
                monitoring_description = 'monitoring description',
                weekly_hours = 10,
                total_value_to_pay = 1000000,
                is_unique_payment = True,
                created_by=user
            )
        # Try to create a moniting contract request with a wrong monitoring type
        with self.assertRaises(ValidationError):
            monitoring_contract_request = MonitoringContractRequest.objects.create_contract_request(
                estimated_completion_date='2021-12-31',
                assigned_to=user,
                cenco = 'cenco',
                has_money_in_cenco = True,
                cenco_manager = 'cenco manager',
                monitoring_type = 'wrong',
                student_code = 'student code',
                student_full_name = 'student full name',
                student_id = 'student id',
                student_email = 'student@example.com',
                student_cellphone = '1234567890',
                daviplata = 'daviplata',
                course_or_proyect = 'course',
                monitoring_description = 'monitoring description',
                weekly_hours = 10,
                total_value_to_pay = 1000000,
                is_unique_payment = True,
                created_by=user
            )

    def test_transition_state_on_monitoring_contract_request(self):
        User = get_user_model()
        # Create a user
        user = User.objects.create_user(id=1, password='1', first_name='John', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')
        # Create a monitoring contract request
        monitoring_contract_request = MonitoringContractRequest.objects.create_contract_request(
            estimated_completion_date='2021-12-31',
            cenco = 'cenco',
            has_money_in_cenco = True,
            cenco_manager = 'cenco manager',
            monitoring_type = 'academic',
            student_code = 'student code',
            student_full_name = 'student full name',
            student_id = 'student id',
            student_email = 'student@example.com',
            student_cellphone = '1234567890',
            daviplata = 'daviplata',
            course_or_proyect = 'course',
            monitoring_description = 'monitoring description',
            weekly_hours = 10,
            total_value_to_pay = 1000000,
            is_unique_payment = True,
            created_by=user
        )
        # Transition the state of the contract request
        monitoring_contract_request.transition_to_state('review', 'Review comment')
        self.assertEqual(monitoring_contract_request.state, 'review')
        # Check that the snapshot was created
        snapshots = monitoring_contract_request.get_snapshots()
        self.assertEqual(snapshots.count(), 1)
        self.assertEqual(snapshots[0].state, 'pending')
        self.assertEqual(snapshots[0].comment, 'Initial comment')
        # Try to transition the state of the contract request to the same state
        with self.assertRaises(ValueError):
            monitoring_contract_request.transition_to_state('review', 'Review comment')
        # Try to transition the state of the contract request to an invalid state
        with self.assertRaises(ValueError):
            monitoring_contract_request.transition_to_state('invalid', 'Invalid comment')
        # Try to transition the state of the contract request to a state that has already been made
        with self.assertRaises(ValueError):
            monitoring_contract_request.transition_to_state('review', 'Review comment')
        # Try to transition the state of the contract request with an invalid state
        with self.assertRaises(ValueError):
            monitoring_contract_request.transition_to_state('invalid', 'Invalid comment')


        