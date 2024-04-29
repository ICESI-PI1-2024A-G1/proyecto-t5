from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class LoginTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)  

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()


    def test_login(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)
