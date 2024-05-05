import time
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class RequestHiringTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)  

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_request_hiring_assing_leader(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)
        
        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')
        
        
        first_cell_text = first_result.find_element(By.XPATH, './td[1]').click()
        
        
        self.assertIn('Solicitud de contratación de', self.selenium.find_element(By.ID, 'titleRequestHiring').text)
        
        select_element = self.selenium.find_element(By.NAME, 'leader')

        select = Select(select_element)

        select.select_by_index(1)
        
        time.sleep(2)
        
        self.assertIn('La solicitud fue exitosa.', self.selenium.find_element(By.ID, 'notificationMessage').text)


    def test_request_hiring_assing_manager(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)
        
        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')
        
        
        first_cell_text = first_result.find_element(By.XPATH, './td[1]').click()
        
        
        self.assertIn('Solicitud de contratación de', self.selenium.find_element(By.ID, 'titleRequestHiring').text)
        
        select_element = self.selenium.find_element(By.NAME, 'manager')

        select = Select(select_element)

        select.select_by_index(1)
        
        time.sleep(2)
        
        self.assertIn('La solicitud fue exitosa.', self.selenium.find_element(By.ID, 'notificationMessage').text)



    def test_request_hiring_change_status(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)
        
        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')
        
        
        first_cell_text = first_result.find_element(By.XPATH, './td[1]').click()
        
        
        self.assertIn('Solicitud de contratación de', self.selenium.find_element(By.ID, 'titleRequestHiring').text)
        
        select_element = self.selenium.find_element(By.ID, 'stateSelect')

        select = Select(select_element)

        select.select_by_index(2)
        
        self.selenium.find_element(By.NAME, 'reason').send_keys("Hola")
        
        
        self.selenium.find_element(By.XPATH, '//input[@type="submit" and @value="Save changes"]').click()

        time.sleep(2)
        
        self.assertIn('75%', self.selenium.find_element(By.ID, 'ProgressBar').text)



    def test_request_hiring_comment(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)
        
        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')
        
        
        first_cell_text = first_result.find_element(By.XPATH, './td[1]').click()
        
        
        self.assertIn('Solicitud de contratación de', self.selenium.find_element(By.ID, 'titleRequestHiring').text)
        
        self.selenium.find_element(By.NAME, 'comment').send_keys("TEXTO DE TEST")

        self.selenium.find_element(By.XPATH, "//button[@value='edit-comment']").click()
        
        time.sleep(2)
        
        self.selenium.refresh()

        time.sleep(2)

        self.assertIn('TEXTO DE TEST', self.selenium.find_element(By.NAME, 'comment').text)




    def test_request_hiring_snapshot(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)
        
        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')
        
        
        first_cell_text = first_result.find_element(By.XPATH, './td[1]').click()
        
        
        self.assertIn('Solicitud de contratación de', self.selenium.find_element(By.ID, 'titleRequestHiring').text)
        

        self.selenium.find_element(By.XPATH, "//button[contains(@onclick, 'view-snapshots-form')]").click()
        
        time.sleep(2)
        
        info = self.selenium.find_element(By.ID, 'pending').text
        
        print(info)

        self.assertIn('Estado de la contratacion:\npending', info)
