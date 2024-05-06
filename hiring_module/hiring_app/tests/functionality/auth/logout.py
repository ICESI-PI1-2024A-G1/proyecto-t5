from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class LogOutTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)  

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_logout_admin(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        button_profile = self.selenium.find_element(By.ID, 'profilePhoto')

        button_profile.click()

        button_logOut1 = self.selenium.find_element(By.ID, 'logoutButton1')

        button_logOut1.click()

        button_logOut2 = self.selenium.find_element(By.ID, 'logoutButton2')

        button_logOut2.click()
        
        self.assertIn('Log In', self.selenium.title)


    def test_logout_leader(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1107838593')
        password_input.send_keys('alejandrolondono123')
        
        password_input.send_keys(Keys.RETURN)
        
        button_profile = self.selenium.find_element(By.ID, 'profilePhoto')

        button_profile.click()

        button_logOut1 = self.selenium.find_element(By.ID, 'logoutButton1')

        button_logOut1.click()

        button_logOut2 = self.selenium.find_element(By.ID, 'logoutButton2')

        button_logOut2.click()
        
        self.assertIn('Log In', self.selenium.title)

    def test_logout_manager(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1111539567')
        password_input.send_keys('santiagovalencia123')
        
        password_input.send_keys(Keys.RETURN)
        
        button_profile = self.selenium.find_element(By.ID, 'profilePhoto')

        button_profile.click()

        button_logOut1 = self.selenium.find_element(By.ID, 'logoutButton1')

        button_logOut1.click()

        button_logOut2 = self.selenium.find_element(By.ID, 'logoutButton2')

        button_logOut2.click()
        
        self.assertIn('Log In', self.selenium.title)
        
        
    def test_logout_external_user(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1106293874')
        password_input.send_keys('mariagonzales123')
        
        password_input.send_keys(Keys.RETURN)
        
        button_profile = self.selenium.find_element(By.ID, 'profilePhoto')

        button_profile.click()

        button_logOut1 = self.selenium.find_element(By.ID, 'logoutButton1')

        button_logOut1.click()

        button_logOut2 = self.selenium.find_element(By.ID, 'logoutButton2')

        button_logOut2.click()
        
        self.assertIn('Log In', self.selenium.title)
