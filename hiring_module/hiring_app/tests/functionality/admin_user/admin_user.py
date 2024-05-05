from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException

class AdminUserTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)  

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

        
    def test_add_user(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        self.assertIn('Panel de control de Administrador', self.selenium.title)



        self.selenium.find_element(By.ID, 'UserList').click()

        time.sleep(2)
        self.assertEqual('Panel de control', self.selenium.title)

                
        self.selenium.find_element(By.ID, 'addUser').click()
        
        
        list_user = self.selenium.find_element(By.ID, 'titleAdd').text
        self.assertIn('Usuarios externos', list_user)
        
        
        self.selenium.find_element(By.ID, '1106293874').click()
        time.sleep(2)
        
        
        user = self.selenium.find_element(By.ID, '1106293874').text

        self.assertIn('1106293874', user)

        

    def test_delete_user(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME, 'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        self.assertIn('Panel de control de Administrador', self.selenium.title)

        try:
            self.selenium.find_element(By.ID, 'UserList').click()
        except StaleElementReferenceException:
            self.selenium.find_element(By.ID, 'UserList').click()

        time.sleep(2)
        self.assertEqual('Panel de control', self.selenium.title)
        
        self.selenium.find_element(By.ID, 'roleSelect_1109185879').send_keys('remove')
        
        
        try:
            self.selenium.find_element(By.ID, 'addUser').click()
        except StaleElementReferenceException:
            self.selenium.find_element(By.ID, 'addUser').click()

        self.assertEqual('1109185879', self.selenium.find_element(By.ID, '1109185879_id').text)

