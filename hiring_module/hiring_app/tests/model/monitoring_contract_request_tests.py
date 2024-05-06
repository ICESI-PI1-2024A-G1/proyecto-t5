from django.test import TestCase
from django.core.exceptions import ValidationError
from hiring_app.model import MonitoringContractRequest
from django.contrib.auth import get_user_model

class MonitoringContractRequestTests(TestCase):
    def create_user1(self):
        User = get_user_model()
        return User.objects.create_user(id=1, password='1', first_name='John', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')
    
    def create_user2(self):
        User = get_user_model()
        return User.objects.create_user(id=2, password='2', first_name='Jane', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')
    
    def create_monitoring_contract_request(self):
        User = get_user_model()
        # Create a user
        user = self.create_user1()
        return MonitoringContractRequest.objects.create_contract_request(
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
                                        
    def test_create_monitoring_contract_request(self):
        # Create a user
        user = self.create_user1()
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
        self.assertEqual(monitoring_contract_request.created_by, user)

    def test_assign_responsibles_to_monitoring_contract_request(self):
        # Create users
        user = self.create_user1()
        user2 = self.create_user2()
        # Create a monitoring contract request
        monitoring_contract_request = self.create_monitoring_contract_request()
        # Assign the user as leader to the contract request
        monitoring_contract_request.assign_leader(user2)
        self.assertEqual(monitoring_contract_request.leader_assigned_to, user2)
        # Assign the user as manager to the contract request
        monitoring_contract_request.assign_manager(user)
        self.assertEqual(monitoring_contract_request.manager_assigned_to, user)

    def test_create_monitoring_contract_request_without_required_fields(self):
        # Try to create a monitoring contract request without the required fields
        with self.assertRaises(ValidationError):
            monitoring_contract_request = MonitoringContractRequest.objects.create_contract_request()

    def test_create_monitoring_contract_request_with_invalid_fields(self):
        user = self.create_user1()
        # Try to create a monitoring contract request with a wrong email
        with self.assertRaises(ValidationError):
            monitoring_contract_request = MonitoringContractRequest.objects.create_contract_request(
                estimated_completion_date='2021-12-31',
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
        # Create monitoring contract request
        monitoring_contract_request = self.create_monitoring_contract_request()
        # Check if there's a snapshot of the contract request
        snapshots = monitoring_contract_request.get_snapshots()
        self.assertEqual(snapshots.count(), 1)
        monitoring_contract_request.transition_to_state('review', 'Review comment')
        self.assertEqual(monitoring_contract_request.state, 'review')
        # Check that the snapshot was created
        snapshots = monitoring_contract_request.get_snapshots()
        self.assertEqual(snapshots.count(), 2)
        self.assertEqual(snapshots[1].state, 'review')
        self.assertEqual(snapshots[1].comment, 'Review comment')

    def test_transition_state_on_monitoring_contract_request(self):
        # Create monitoring contract request
        monitoring_contract_request = self.create_monitoring_contract_request()
        monitoring_contract_request.transition_to_state('review', 'Review comment')
        # Try to transition the state of the contract request to the same state
        with self.assertRaises(ValueError):
            monitoring_contract_request.transition_to_state('review', 'Review comment')

    def test_transition_to_invalid_state_on_monitoring_contract_request(self):
        # Create monitoring contract request
        monitoring_contract_request = self.create_monitoring_contract_request()
        # Try to transition the state of the contract request to an invalid state
        with self.assertRaises(ValueError):
            monitoring_contract_request.transition_to_state('invalid', 'Invalid comment')

    def test_transition_to_already_made_state_on_monitoring_contract_request(self):
        # Create monitoring contract request
        monitoring_contract_request = self.create_monitoring_contract_request()
        monitoring_contract_request.transition_to_state('review', 'Review comment')
        # Try to transition the state of the contract request to a state that has already been made
        with self.assertRaises(ValueError):
            monitoring_contract_request.transition_to_state('pending', 'pending comment')     


        