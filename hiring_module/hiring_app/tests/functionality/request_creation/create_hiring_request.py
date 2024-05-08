from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

class CreateHiringRequest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)  

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

        
    def test_create_form_monitoring(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1106293874')
        password_input.send_keys('mariagonzales123')
        
        password_input.send_keys(Keys.RETURN)
        
        button_create_monitoring_contract = self.selenium.find_element(By.ID, 'create_monitoring_contract')

        button_create_monitoring_contract.click()
        self.selenium.find_element(By.NAME, 'cenco').send_keys('Cenco ABC')
        self.selenium.find_element(By.NAME, 'cenco_manager').send_keys('John Doe')
        monitoring_type = self.selenium.find_element(By.NAME, 'monitoring_type')
        monitoring_type.send_keys('Academic')
        self.selenium.find_element(By.NAME, 'student_code').send_keys('123456')
        self.selenium.find_element(By.NAME, 'student_full_name').send_keys('Jane Smith')
        self.selenium.find_element(By.NAME, 'student_id').send_keys('7890123')
        self.selenium.find_element(By.NAME, 'student_email').send_keys('jane@example.com')
        self.selenium.find_element(By.NAME, 'student_cellphone').send_keys('1234567890')
        self.selenium.find_element(By.NAME, 'daviplata').send_keys('Daviplata XYZ')
        self.selenium.find_element(By.NAME, 'course_or_proyect').send_keys('Project ABC')
        self.selenium.find_element(By.NAME, 'monitoring_description').send_keys('Description of monitoring')
        self.selenium.find_element(By.NAME, 'weekly_hours').send_keys('10')  # Assuming 10 weekly hours
        self.selenium.find_element(By.NAME, 'total_value_to_pay').send_keys('100000')  # Assuming total value
        self.selenium.find_element(By.NAME, 'is_unique_payment').click()
        self.selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(5)
        notification_message = self.selenium.find_element(By.ID, "notificationMessage").text
        
        self.assertEqual(notification_message, "La solicitud fue exitosa.")

        self.assertIn('Solicitudes de contratos de Monitoría', self.selenium.title)


    def test_create_form_cex(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1106293874')
        password_input.send_keys('mariagonzales123')
        
        password_input.send_keys(Keys.RETURN)
        
        button_create_monitoring_contract = self.selenium.find_element(By.ID, 'create_cex_contract')

        button_create_monitoring_contract.click()
        
        self.selenium.find_element(By.NAME, 'solicitant_name').send_keys('John Doe')
        self.selenium.find_element(By.NAME, 'solicitant_faculty').send_keys('Faculty of Engineering')
        self.selenium.find_element(By.NAME, 'hiree_full_name').send_keys('Jane Smith')
        self.selenium.find_element(By.NAME, 'hiree_id').send_keys('123456789')
        self.selenium.find_element(By.NAME, 'hiree_cellphone').send_keys('1234567890')
        self.selenium.find_element(By.NAME, 'hiree_email').send_keys('jane@example.com')
        self.selenium.find_element(By.NAME, 'cenco').send_keys('Cenco 123')
        self.selenium.find_element(By.NAME, 'request_motive').send_keys('Hiring new employee')
        self.selenium.find_element(By.NAME, 'banking_entity').send_keys('Bank of Example')
        bank_account_type = self.selenium.find_element(By.NAME, 'bank_account_type')
        bank_account_type.send_keys('Savings') 
        self.selenium.find_element(By.NAME, 'bank_account_number').send_keys('1234567890')
        self.selenium.find_element(By.NAME, 'eps').send_keys('EPS Company')
        self.selenium.find_element(By.NAME, 'pension_fund').send_keys('Pension Fund')
        self.selenium.find_element(By.NAME, 'arl').send_keys('ARL Company')
        self.selenium.find_element(By.NAME, 'contract_value').send_keys('1000000') 
        self.selenium.find_element(By.NAME, 'charge_account').send_keys('Charge account details')
        ruta_documento_pdf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'documento.pdf')

        self.selenium.find_element(By.NAME, 'rut').send_keys(ruta_documento_pdf)

        self.selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(2)
        notification_message = self.selenium.find_element(By.ID, "notificationMessage").text
        
        self.assertEqual(notification_message, "La solicitud fue exitosa.")

        self.assertIn('Solicitudes de contratos CEX', self.selenium.title)


    def test_create_form_pos(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1106293874')
        password_input.send_keys('mariagonzales123')
        
        password_input.send_keys(Keys.RETURN)
        
        button_create_pos_contract = self.selenium.find_element(By.ID, 'create_pos_contract')

        button_create_pos_contract.click()
        
        self.selenium.find_element(By.NAME, 'solicitant_name').send_keys('John Doe')
        self.selenium.find_element(By.NAME, 'solicitant_faculty').send_keys('Faculty of Engineering')
        self.selenium.find_element(By.NAME, 'hiree_full_name').send_keys('Jane Smith')
        self.selenium.find_element(By.NAME, 'hiree_id').send_keys('123456789')
        self.selenium.find_element(By.NAME, 'hiree_cellphone').send_keys('1234567890')
        self.selenium.find_element(By.NAME, 'hiree_email').send_keys('jane@example.com')
        self.selenium.find_element(By.NAME, 'cenco').send_keys('Cenco 123')
        self.selenium.find_element(By.NAME, 'request_motive').send_keys('Hiring new employee')
        self.selenium.find_element(By.NAME, 'banking_entity').send_keys('Bank of Example')
        bank_account_type = self.selenium.find_element(By.NAME, 'bank_account_type')
        bank_account_type.send_keys('Savings') 
        self.selenium.find_element(By.NAME, 'bank_account_number').send_keys('1234567890')
        self.selenium.find_element(By.NAME, 'eps').send_keys('EPS Company')
        self.selenium.find_element(By.NAME, 'pension_fund').send_keys('Pension Fund')
        self.selenium.find_element(By.NAME, 'arl').send_keys('ARL Company')
        self.selenium.find_element(By.NAME, 'contract_value').send_keys('1000000') 
        self.selenium.find_element(By.NAME, 'charge_account').send_keys('Charge account details')
        ruta_documento_pdf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'documento.pdf')

        self.selenium.find_element(By.NAME, 'rut').send_keys(ruta_documento_pdf)
        self.selenium.find_element(By.NAME, 'course_name').send_keys('Computer Science')
        self.selenium.find_element(By.NAME, 'period').send_keys('2024 Spring')
        self.selenium.find_element(By.NAME, 'group').send_keys('Group A')
        self.selenium.find_element(By.NAME, 'intensity').send_keys('20')
        self.selenium.find_element(By.NAME, 'total_hours').send_keys('40')
        self.selenium.find_element(By.NAME, 'course_code').send_keys('CS101')
        self.selenium.find_element(By.NAME, 'students_quantity').send_keys('30')
        self.selenium.find_element(By.NAME, 'additional_hours').send_keys('10')
        additional_fields = self.selenium.find_elements(By.XPATH, '//div[@id="additionalFields"]')
        for field in additional_fields:
            field.find_element(By.CSS_SELECTOR, "[name^='additionalFields-date']").send_keys('2024-05-04')
            field.find_element(By.CSS_SELECTOR, "[name^='additionalFields-start_time']").send_keys('08:001')  # 1 para AM
            field.find_element(By.CSS_SELECTOR, "[name^='additionalFields-end_time']").send_keys('12:002')    # 2 para PM
            field.find_element(By.CSS_SELECTOR, "[name^='additionalFields-room']").send_keys('101D')
            field.find_element(By.CSS_SELECTOR, "[name^='additionalFields-responsability']").send_keys('Teaching')

        self.selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(4)
        notification_message = self.selenium.find_element(By.ID, "notificationMessage").text
        
        self.assertEqual(notification_message, "La solicitud fue exitosa.")
        self.assertIn('Solicitudes de contratos POS', self.selenium.title)
