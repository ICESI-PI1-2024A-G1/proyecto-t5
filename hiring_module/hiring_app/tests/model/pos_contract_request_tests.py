from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from hiring_app.model import ProvisionOfServicesContractRequest

class ProvisionOfServicesContractRequestTests(TestCase):
    def test_create_pos_contract_request(self):
        User = get_user_model()
        # Create a user
        user = User.objects.create_user(id=1, password='1', first_name='John', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')
        user2 = User.objects.create_user(id=2, password='2', first_name='Jane', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')
        # Create a pos contract request
        pos_contract_request = ProvisionOfServicesContractRequest.objects.create_contract_request(
            estimated_completion_date='2021-12-31',
            hiree_full_name='Jane Doe',
            hiree_id=148964,
            hiree_cellphone='1234567890',
            hiree_email='janedoe@example.com',
            cenco='cenco',
            request_motive='Request motive',
            banking_entity='Banking entity',
            bank_account_type='savings',
            bank_account_number='1234567890',
            eps='EPS',
            pension_fund='Pension fund',
            arl='ARL',
            contract_value=123456,
            charge_account='Charge account',
            rut=f'rut content',
            created_by=user,
            course_name = "Yo",
            period = "Periodo",
            group = "5",
            intensity = 20,
            total_hours = 20,
            course_code = "123456789",
            students_quantity = 10,
            additional_hours = 0,
            course_schedules=[
                {
                    'date': '2021-12-31',
                    'start_time': '08:00',
                    'end_time': '12:00',
                    'room': 'Room 1',
                    'responsability': 'Responsability 1'
                },
                {
                    'date': '2021-12-31',
                    'start_time': '14:00',
                    'end_time': '18:00',
                    'room': 'Room 2',
                    'responsability': 'Responsability 2'
                }
            ]
        )
        self.assertEqual(pos_contract_request.hiree_full_name, 'Jane Doe')
        self.assertEqual(pos_contract_request.hiree_id, 148964)
        self.assertEqual(pos_contract_request.hiree_cellphone, '1234567890')
        self.assertEqual(pos_contract_request.hiree_email, 'janedoe@example.com')
        self.assertEqual(pos_contract_request.cenco, 'cenco')
        self.assertEqual(pos_contract_request.request_motive, 'Request motive')
        self.assertEqual(pos_contract_request.banking_entity, 'Banking entity')
        self.assertEqual(pos_contract_request.bank_account_type, 'savings')
        self.assertEqual(pos_contract_request.bank_account_number, '1234567890')
        self.assertEqual(pos_contract_request.eps, 'EPS')
        self.assertEqual(pos_contract_request.pension_fund, 'Pension fund')
        self.assertEqual(pos_contract_request.arl, 'ARL')
        self.assertEqual(pos_contract_request.contract_value, 123456)
        self.assertEqual(pos_contract_request.charge_account, 'Charge account')
        self.assertEqual(pos_contract_request.rut, f'rut content')
        self.assertEqual(pos_contract_request.created_by, user)
        # Assign the user as leader to the contract request
        pos_contract_request.assign_leader(user2)
        self.assertEqual(pos_contract_request.leader_assigned_to, user2)
        # Assign the user as manager to the contract request
        pos_contract_request.assign_manager(user)
        self.assertEqual(pos_contract_request.manager_assigned_to, user)
        # Try to create a pos contract request without the required fields
        with self.assertRaises(ValidationError):
            pos_contract_request = ProvisionOfServicesContractRequest.objects.create_contract_request(
                course_schedules=[
                    {
                        'date': '2021-12-31',
                        'start_time': '08:00',
                        'end_time': '12:00',
                        'room': 'Room 1',
                        'responsability': 'Responsability 1'
                    },
                    {
                        'date': '2021-12-31',
                        'start_time': '14:00',
                        'end_time': '18:00',
                        'room': 'Room 2',
                        'responsability': 'Responsability 2'
                    }
                ]
            )
        # Try to create a pos contract with a wrong bank account type
        with self.assertRaises(ValidationError):
            pos_contract_request = ProvisionOfServicesContractRequest.objects.create_contract_request(
                estimated_completion_date='2021-12-31',
            hiree_full_name='Jane Doe',
            hiree_id=148964,
            hiree_cellphone='1234567890',
            hiree_email='janedoe@example.com',
            cenco='cenco',
            request_motive='Request motive',
            banking_entity='Banking entity',
            bank_account_type='sav',
            bank_account_number='1234567890',
            eps='EPS',
            pension_fund='Pension fund',
            arl='ARL',
            contract_value=123456,
            charge_account='Charge account',
            rut=f'rut content',
            created_by=user,
            course_name = "Yo",
            period = "Periodo",
            group = "5",
            intensity = 20,
            total_hours = 20,
            course_code = "123456789",
            students_quantity = 10,
            additional_hours = 0,
            course_schedules=[
                {
                    'date': '2021-12-31',
                    'start_time': '08:00',
                    'end_time': '12:00',
                    'room': 'Room 1',
                    'responsability': 'Responsability 1'
                },
                {
                    'date': '2021-12-31',
                    'start_time': '14:00',
                    'end_time': '18:00',
                    'room': 'Room 2',
                    'responsability': 'Responsability 2'
                }
            ]
            )
        # Try to create a pos contract with a wrong email
        with self.assertRaises(ValidationError):
            pos_contract_request = ProvisionOfServicesContractRequest.objects.create_contract_request(
                estimated_completion_date='2021-12-31',
            hiree_full_name='Jane Doe',
            hiree_id=148964,
            hiree_cellphone='1234567890',
            hiree_email='janedoxample.com',
            cenco='cenco',
            request_motive='Request motive',
            banking_entity='Banking entity',
            bank_account_type='savings',
            bank_account_number='1234567890',
            eps='EPS',
            pension_fund='Pension fund',
            arl='ARL',
            contract_value=123456,
            charge_account='Charge account',
            rut=f'rut content',
            created_by=user,
            course_name = "Yo",
            period = "Periodo",
            group = "5",
            intensity = 20,
            total_hours = 20,
            course_code = "123456789",
            students_quantity = 10,
            additional_hours = 0,
            course_schedules=[
                {
                    'date': '2021-12-31',
                    'start_time': '08:00',
                    'end_time': '12:00',
                    'room': 'Room 1',
                    'responsability': 'Responsability 1'
                },
                {
                    'date': '2021-12-31',
                    'start_time': '14:00',
                    'end_time': '18:00',
                    'room': 'Room 2',
                    'responsability': 'Responsability 2'
                }
            ]
            )
    
    def test_transition_state_on_pos_contract_request(self):
        User = get_user_model()
        # Create a user
        user = User.objects.create_user(id=1, password='1', first_name='John', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')
        # Create a pos contract request
        pos_contract_request = ProvisionOfServicesContractRequest.objects.create_contract_request(
            estimated_completion_date='2021-12-31',
            hiree_full_name='Jane Doe',
            hiree_id=148964,
            hiree_cellphone='1234567890',
            hiree_email='janedoe@example.com',
            cenco='cenco',
            request_motive='Request motive',
            banking_entity='Banking entity',
            bank_account_type='savings',
            bank_account_number='1234567890',
            eps='EPS',
            pension_fund='Pension fund',
            arl='ARL',
            contract_value=123456,
            charge_account='Charge account',
            rut=f'rut content',
            created_by=user,
            course_name = "Yo",
            period = "Periodo",
            group = "5",
            intensity = 20,
            total_hours = 20,
            course_code = "123456789",
            students_quantity = 10,
            additional_hours = 0,
            course_schedules=[
                {
                    'date': '2021-12-31',
                    'start_time': '08:00',
                    'end_time': '12:00',
                    'room': 'Room 1',
                    'responsability': 'Responsability 1'
                },
                {
                    'date': '2021-12-31',
                    'start_time': '14:00',
                    'end_time': '18:00',
                    'room': 'Room 2',
                    'responsability': 'Responsability 2'
                }
            ]
        )
        # Check if there's a snapshot of the contract request
        snapshots = pos_contract_request.get_snapshots()
        self.assertEqual(snapshots.count(), 1)
        pos_contract_request.transition_to_state('review', 'Review comment')
        self.assertEqual(pos_contract_request.state, 'review')
        # Check that the snapshot was created
        snapshots = pos_contract_request.get_snapshots()
        self.assertEqual(snapshots.count(), 2)
        self.assertEqual(snapshots[1].state, 'review')
        self.assertEqual(snapshots[1].comment, 'Review comment')
        # Try to transition the state of the contract request to the same state
        with self.assertRaises(ValueError):
            pos_contract_request.transition_to_state('review', 'Review comment')
        # Try to transition the state of the contract request to an invalid state
        with self.assertRaises(ValueError):
            pos_contract_request.transition_to_state('invalid', 'Invalid comment')
        # Try to transition the state of the contract request to a state that has already been made
        with self.assertRaises(ValueError):
            pos_contract_request.transition_to_state('pending', 'pending comment')        