from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class ControlBoardExternalUser(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)  

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

        
    def test_get_form_monitoring(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1106293874')
        password_input.send_keys('mariagonzales123')
        
        password_input.send_keys(Keys.RETURN)
        
        button_create_monitoring_contract = self.selenium.find_element(By.ID, 'create_monitoring_contract')

        button_create_monitoring_contract.click()
        
        
        self.assertIn('Solicitudes de contratos de Monitoría', self.selenium.title)


    def test_get_form_cex(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1106293874')
        password_input.send_keys('mariagonzales123')
        
        password_input.send_keys(Keys.RETURN)
        
        button_create_monitoring_contract = self.selenium.find_element(By.ID, 'create_cex_contract')

        button_create_monitoring_contract.click()
        
        
        self.assertIn('Solicitudes de contratos CEX', self.selenium.title)


    def test_get_form_pos(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1106293874')
        password_input.send_keys('mariagonzales123')
        
        password_input.send_keys(Keys.RETURN)
        
        button_create_pos_contract = self.selenium.find_element(By.ID, 'create_pos_contract')

        button_create_pos_contract.click()
        
        
        self.assertIn('Solicitudes de contratos POS', self.selenium.title)
