from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def send_text_to_element(self,locator_type,locator,password):
        self.driver.find_element(locator_type, locator).send_keys(password)

    def click_on_element(self, locator_type,locator):
        self.driver.find_element(locator_type,locator).click()
