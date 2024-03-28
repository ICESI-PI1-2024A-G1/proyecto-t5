from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from hiring_app.model import CEXContractRequest

class CEXContractRequestModelTests(TestCase):
    def test_create_cex_contract_request(self):
        User = get_user_model()
        # Create a user
        user = User.objects.create_user(id=1, password='1', first_name='John', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')
        user2 = User.objects.create_user(id=2, password='2', first_name='Jane', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')
        # Create a CEX contract request
        cex_contract_request = CEXContractRequest.objects.create_contract_request(
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
            created_by=user
        )
        self.assertEqual(cex_contract_request.hiree_full_name, 'Jane Doe')
        self.assertEqual(cex_contract_request.hiree_id, 148964)
        self.assertEqual(cex_contract_request.hiree_cellphone, '1234567890')
        self.assertEqual(cex_contract_request.hiree_email, 'janedoe@example.com')
        self.assertEqual(cex_contract_request.cenco, 'cenco')
        self.assertEqual(cex_contract_request.request_motive, 'Request motive')
        self.assertEqual(cex_contract_request.banking_entity, 'Banking entity')
        self.assertEqual(cex_contract_request.bank_account_type, 'savings')
        self.assertEqual(cex_contract_request.bank_account_number, '1234567890')
        self.assertEqual(cex_contract_request.eps, 'EPS')
        self.assertEqual(cex_contract_request.pension_fund, 'Pension fund')
        self.assertEqual(cex_contract_request.arl, 'ARL')
        self.assertEqual(cex_contract_request.contract_value, 123456)
        self.assertEqual(cex_contract_request.charge_account, 'Charge account')
        self.assertEqual(cex_contract_request.rut, f'rut content')
        self.assertEqual(cex_contract_request.created_by, user)
        # Assign the user as leader to the contract request
        cex_contract_request.assign_leader(user2)
        self.assertEqual(cex_contract_request.leader_assigned_to, user2)
        # Assign the user as manager to the contract request
        cex_contract_request.assign_manager(user)
        self.assertEqual(cex_contract_request.manager_assigned_to, user)
        # Try to create a CEX contract request without the required fields
        with self.assertRaises(ValidationError):
            cex_contract_request = CEXContractRequest.objects.create_contract_request()
        # Try to create a CEX contract with a wrong bank account type
        with self.assertRaises(ValidationError):
            cex_contract_request = CEXContractRequest.objects.create_contract_request(
                estimated_completion_date='2021-12-31',
                hiree_full_name='Jane Doe',
                hiree_id=148964,
                hiree_cellphone='1234567890',
                hiree_email='janedoe@example.com',
                cenco='cenco',
                request_motive='Request motive',
                banking_entity='Banking entity',
                bank_account_type='checks',
                bank_account_number='1234567890',
                eps='EPS',
                pension_fund='Pension fund',
                arl='ARL',
                contract_value=123456,
                charge_account='Charge account',
                rut=f'rut content',
                created_by=user
            )
        # Try to create a CEX contract with a wrong email
        with self.assertRaises(ValidationError):
            cex_contract_request = CEXContractRequest.objects.create_contract_request(
                estimated_completion_date='2021-12-31',
                hiree_full_name='Jane Doe',
                hiree_id=148964,
                hiree_cellphone='1234567890',
                hiree_email='janedoe',
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
                created_by=user
            )
    
    def test_transition_state_on_cex_contract_request(self):
        User = get_user_model()
        # Create a user
        user = User.objects.create_user(id=1, password='1', first_name='John', last_name='Doe', birth_date='1990-01-01', address='1234 Main St')
        # Create a CEX contract request
        cex_contract_request = CEXContractRequest.objects.create_contract_request(
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
            created_by=user
        )
        # Check if there's a snapshot of the contract request
        snapshots = cex_contract_request.get_snapshots()
        self.assertEqual(snapshots.count(), 1)
        cex_contract_request.transition_to_state('review', 'Review comment')
        self.assertEqual(cex_contract_request.state, 'review')
        # Check that the snapshot was created
        snapshots = cex_contract_request.get_snapshots()
        self.assertEqual(snapshots.count(), 2)
        self.assertEqual(snapshots[1].state, 'review')
        self.assertEqual(snapshots[1].comment, 'Review comment')
        # Try to transition the state of the contract request to the same state
        with self.assertRaises(ValueError):
            cex_contract_request.transition_to_state('review', 'Review comment')
        # Try to transition the state of the contract request to an invalid state
        with self.assertRaises(ValueError):
            cex_contract_request.transition_to_state('invalid', 'Invalid comment')
        # Try to transition the state of the contract request to a state that has already been made
        with self.assertRaises(ValueError):
            cex_contract_request.transition_to_state('pending', 'pending comment')        