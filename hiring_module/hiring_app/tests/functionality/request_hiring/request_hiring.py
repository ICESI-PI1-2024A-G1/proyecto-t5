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

    def test_search_request_hiring_by_id(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)
        
        search_input = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="search"]')

        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')

        id = first_result.find_element(By.XPATH, './td[1]').text

        search_input.send_keys(id)

        search_input.send_keys(Keys.RETURN)
        
        self.assertIn(id, self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]/td[1]').text)

    def test_search_request_hiring_by_solicitant(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)
        
        search_input = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="search"]')

        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')

        id = first_result.find_element(By.XPATH, './td[1]').text

        solicitant = first_result.find_element(By.XPATH, './td[2]').text

        search_input.send_keys(solicitant)

        search_input.send_keys(Keys.RETURN)
        
        self.assertIn(id, self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]/td[1]').text)

    def test_search_request_hiring_by_state(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)
        
        search_input = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="search"]')

        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')

        id = first_result.find_element(By.XPATH, './td[1]').text

        state = "Pendiente"

        search_input.send_keys(state)

        search_input.send_keys(Keys.RETURN)
        
        self.assertIn(id, self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]/td[1]').text)

    def test_search_request_hiring_by_date(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)
        
        search_input = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="search"]')

        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')

        id = first_result.find_element(By.XPATH, './td[1]').text

        date = first_result.find_element(By.XPATH, './td[6]').text

        search_input.send_keys(date)

        search_input.send_keys(Keys.RETURN)
        
        self.assertIn(id, self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]/td[1]').text)

    def test_search_request_hiring_by_wrong_id(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)
        
        search_input = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="search"]')

        search_input.send_keys('abcdef-abcdef-abcdef')

        search_input.send_keys(Keys.RETURN)
        
        self.assertIn('No matching records found', self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr/td').text)

    def test_access_request_hiring(self):
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

    def test_request_hiring_change_status_pending_review_filled(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)

        search_input = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="search"]')

        search_input.send_keys("Pendiente")

        search_input.send_keys(Keys.RETURN)
        
        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')
        
        
        first_cell_text = first_result.find_element(By.XPATH, './td[1]').click()
        
        
        self.assertIn('Solicitud de contratación de', self.selenium.find_element(By.ID, 'titleRequestHiring').text)
        
        select_element = self.selenium.find_element(By.ID, 'stateSelect')

        select = Select(select_element)

        # 1 = review
        # 2 = incomplete
        # 3 = Filed
        # 4 = Cancelled

        select.select_by_index(1)
        

        time.sleep(2)
        
        self.assertIn('50%', self.selenium.find_element(By.ID, 'ProgressBar').text)

        with self.assertRaises(NotImplementedError):
            select_element = self.selenium.find_element(By.ID, 'stateSelect')

            select = Select(select_element)

            select.select_by_index(2)

        select_element = self.selenium.find_element(By.ID, 'stateSelect')

        select = Select(select_element)

        select.select_by_index(3)

        self.assertIn('100%', self.selenium.find_element(By.ID, 'ProgressBar').text)

    def test_request_hiring_change_status_pending_incomplete_cancelled(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)

        search_input = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="search"]')

        search_input.send_keys("Pendiente")

        search_input.send_keys(Keys.RETURN)
        
        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')
        
        
        first_cell_text = first_result.find_element(By.XPATH, './td[1]').click()
        
        
        self.assertIn('Solicitud de contratación de', self.selenium.find_element(By.ID, 'titleRequestHiring').text)
        
        select_element = self.selenium.find_element(By.ID, 'stateSelect')

        select = Select(select_element)

        # 1 = review
        # 2 = incomplete
        # 3 = Filed
        # 4 = Cancelled

        select.select_by_index(2)

        self.selenium.find_element(By.NAME, 'reason').send_keys("Hola")
        
        self.selenium.find_element(By.XPATH, '//input[@type="submit" and @value="Enviar"]').click()

        time.sleep(2)
        
        self.assertIn('75%', self.selenium.find_element(By.ID, 'ProgressBar').text)

        select_element = self.selenium.find_element(By.ID, 'stateSelect')

        select = Select(select_element)

        select.select_by_index(4)

        self.selenium.find_element(By.NAME, 'reason').send_keys("Hola")

        self.selenium.find_element(By.XPATH, '//input[@type="submit" and @value="Enviar"]').click()

        self.assertIn('100%', self.selenium.find_element(By.ID, 'ProgressBar').text)

    
    def test_request_hiring_change_status_pending_incomplete_review_cancelled(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)

        search_input = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="search"]')

        search_input.send_keys("Pendiente")

        search_input.send_keys(Keys.RETURN)
        
        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')
        
        
        first_cell_text = first_result.find_element(By.XPATH, './td[1]').click()
        
        self.assertIn('Solicitud de contratación de', self.selenium.find_element(By.ID, 'titleRequestHiring').text)
        
        select_element = self.selenium.find_element(By.ID, 'stateSelect')

        select = Select(select_element)

        # 1 = review
        # 2 = incomplete
        # 3 = Filed
        # 4 = Cancelled


        with self.assertRaises(NotImplementedError):
            select.select_by_index(3)

        select.select_by_index(2)

        self.selenium.find_element(By.NAME, 'reason').send_keys("Hola")
        
        self.selenium.find_element(By.XPATH, '//input[@type="submit" and @value="Enviar"]').click()
        
        self.assertIn('75%', self.selenium.find_element(By.ID, 'ProgressBar').text)

        with self.assertRaises(NotImplementedError):
            select_element = self.selenium.find_element(By.ID, 'stateSelect')

            select = Select(select_element)

            select.select_by_index(3)

        select_element = self.selenium.find_element(By.ID, 'stateSelect')

        select = Select(select_element)

        select.select_by_index(1)

        self.assertIn('50%', self.selenium.find_element(By.ID, 'ProgressBar').text)

        select_element = self.selenium.find_element(By.ID, 'stateSelect')

        select = Select(select_element)

        select.select_by_index(4)

        self.selenium.find_element(By.NAME, 'reason').send_keys("Hola")

        self.selenium.find_element(By.XPATH, '//input[@type="submit" and @value="Enviar"]').click()

        self.assertIn('100%', self.selenium.find_element(By.ID, 'ProgressBar').text)

    def test_request_hiring_change_status_pending_cancelled(self):
        self.selenium.get(self.live_server_url)
        
        username_input = self.selenium.find_element(By.NAME,'id')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('1116070867')
        password_input.send_keys('juandiaz123')
        
        password_input.send_keys(Keys.RETURN)
        
        self.assertIn('Panel de control de Administrador', self.selenium.title)

        search_input = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="search"]')

        search_input.send_keys("Pendiente")

        search_input.send_keys(Keys.RETURN)
        
        first_result = self.selenium.find_element(By.XPATH, '//table[@id="dataTable"]/tbody/tr[1]')
        
        
        first_cell_text = first_result.find_element(By.XPATH, './td[1]').click()
        
        self.assertIn('Solicitud de contratación de', self.selenium.find_element(By.ID, 'titleRequestHiring').text)
        
        select_element = self.selenium.find_element(By.ID, 'stateSelect')

        select = Select(select_element)

        # 1 = review
        # 2 = incomplete
        # 3 = Filed
        # 4 = Cancelled

        select.select_by_index(4)

        self.selenium.find_element(By.NAME, 'reason').send_keys("Hola")

        self.selenium.find_element(By.XPATH, '//input[@type="submit" and @value="Enviar"]').click()

        self.assertIn('100%', self.selenium.find_element(By.ID, 'ProgressBar').text)


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
        
        self.assertIn('Estado de la contratacion:\npending', info)
