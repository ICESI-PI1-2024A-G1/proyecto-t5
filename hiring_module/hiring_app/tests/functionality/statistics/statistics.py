from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.select import Select
import time

class StatisticsTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)  

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_date_range_statistics(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)

        statistics_button = self.selenium.find_element(By.ID, 'Statistics')

        statistics_button.click()

        time.sleep(2)

        self.assertIn('Estadísticas', self.selenium.title)

        # Get the current date
        current_date = datetime.now().strftime('%m/%d/%Y')

        # Send the current date to the start_date field
        start_date = self.selenium.find_element(By.ID, 'start_date')
        start_date.send_keys(current_date)

        # Send the current date to the end_date field
        end_date = self.selenium.find_element(By.ID, 'end_date')
        end_date.send_keys(current_date)

        contratos_cex = self.selenium.find_element(By.ID, 'contratos_cex').text
        self.assertIn('4', contratos_cex)

    def test_leader_statistics(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)
        
        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')
        
        
        first_cell_text = first_result.find_element(By.XPATH, './td[1]').click()
        
        time.sleep(2)
        
        self.assertIn('Solicitud de contratación de', self.selenium.find_element(By.ID, 'titleRequestHiring').text)
        
        select_element = self.selenium.find_element(By.NAME, 'leader')

        select = Select(select_element)

        select.select_by_index(1)
        
        time.sleep(2)
        
        self.assertIn('La solicitud fue exitosa.', self.selenium.find_element(By.ID, 'notificationMessage').text)

        notificationCloseBtn = self.selenium.find_element(By.ID, 'notificationCloseBtn')

        notificationCloseBtn.click()

        time.sleep(2)

        
        statistics_button = self.selenium.find_element(By.ID, 'Statistics')

        statistics_button.click()

        time.sleep(2)

        self.assertIn('Estadísticas', self.selenium.title)

        select_element = self.selenium.find_element(By.ID, "data_leader_select")

        select = Select(select_element)

        select.select_by_index(0)

        solicitudes_por_validar_leader = self.selenium.find_element(By.ID, 'solicitudes_por_validar_leader').text

        self.assertIn('1', solicitudes_por_validar_leader)

        time.sleep(2)

    def test_manager_statistics(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)
        
        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')
        
        
        first_cell_text = first_result.find_element(By.XPATH, './td[1]').click()
        
        time.sleep(2)
        
        self.assertIn('Solicitud de contratación de', self.selenium.find_element(By.ID, 'titleRequestHiring').text)
        
        select_element = self.selenium.find_element(By.NAME, 'manager')

        select = Select(select_element)

        select.select_by_index(1)
        
        time.sleep(2)
        
        self.assertIn('La solicitud fue exitosa.', self.selenium.find_element(By.ID, 'notificationMessage').text)

        notificationCloseBtn = self.selenium.find_element(By.ID, 'notificationCloseBtn')

        notificationCloseBtn.click()

        time.sleep(2)
        
        statistics_button = self.selenium.find_element(By.ID, 'Statistics')

        statistics_button.click()

        time.sleep(2)

        self.assertIn('Estadísticas', self.selenium.title)


        select_element = self.selenium.find_element(By.ID, "data_manager_select")

        select = Select(select_element)

        select.select_by_index(0)

        solicitudes_por_validar_leader = self.selenium.find_element(By.ID, 'solicitudes_por_validar_manager').text

        self.assertIn('1', solicitudes_por_validar_leader)

        
        

    