from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LeftPanelNavigation(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)  

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

        
    def test_admin_redirections(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        
        password_input.send_keys(Keys.RETURN)
        
        user_list_button = self.selenium.find_element(By.ID, 'UserList')

        user_list_button.click()
        
        
        self.assertIn('Lista de usuarios', self.selenium.title)

        control_pannel_button = self.selenium.find_element(By.ID, 'ControlPanel')

        control_pannel_button.click()

        self.assertIn('Panel de control', self.selenium.title)

        statistics_button = self.selenium.find_element(By.ID, 'Statistics')

        statistics_button.click()

        self.assertIn('Estadísticas', self.selenium.title)

    def test_leader_redirections(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1107838593')
        password_input.send_keys('alejandrolondono123')


        password_input.send_keys(Keys.RETURN)
        
        with self.assertRaises(NoSuchElementException):
            user_list_button = self.selenium.find_element(By.ID, 'UserList')


        statistics_button = self.selenium.find_element(By.ID, 'Statistics')

        statistics_button.click()

        self.assertIn('Estadísticas', self.selenium.title)

        control_pannel_button = self.selenium.find_element(By.ID, 'ControlPanel')

        control_pannel_button.click()

        self.assertIn('Panel de control', self.selenium.title)

    def test_external_user_redirections(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1106293874')
        password_input.send_keys('mariagonzales123')
        
        password_input.send_keys(Keys.RETURN)
        
        with self.assertRaises(NoSuchElementException):
            user_list_button = self.selenium.find_element(By.ID, 'UserList')

        with self.assertRaises(NoSuchElementException):
            statistics_button = self.selenium.find_element(By.ID, 'Statistics')    

        control_pannel_button = self.selenium.find_element(By.ID, 'ControlPanel')

        control_pannel_button.click()

        self.assertIn('Panel de control', self.selenium.title)
