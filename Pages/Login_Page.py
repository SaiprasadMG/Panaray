from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage
from Utilities import ReadConfigurations


class Login_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    email_field = "//input[@id='formHorizontalEmail']"
    password_field = "//input[@id='formHorizontalPassword']"
    submit_button = "//button[@type='submit']"
    error_message_locator = "//div[@class='errorMzs xx-small-normal']/child::strong[1]"
    error_message = "Email or Password not recognized, try again."
    valid_email = f'{ReadConfigurations.get_config("panaray_prod_valid_credentials", "valid_email")}'
    valid_password = f'{ReadConfigurations.get_config("panaray_prod_valid_credentials", "valid_password")}'

    def enter_email_address(self, email):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.email_field)))
        self.send_text_to_element(By.XPATH,self.email_field,email)

    def enter_password(self, password):
        self.send_text_to_element(By.XPATH, self.password_field, password)
        self.click_on_element(By.XPATH, self.submit_button)

    def display_error_msg(self):
        error_msg = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.error_message_locator)))
        assert error_msg.is_displayed()

    def assert_error_msg(self, expected_text):
        message = self.driver.find_element(By.XPATH, self.error_message_locator).text
        assert message == expected_text

    def login_with_credentials(self, email, password):
        self.enter_email_address(email)
        self.enter_password(password)
