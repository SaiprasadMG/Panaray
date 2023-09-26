from datetime import datetime

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities import ReadConfigurations


# url = ReadConfigurations.get_config("panaray_prod_valid_credentials", "valid_email")
# print(type(url))

# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 20)
# driver.get("https://www.panaray.com/")
# email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='formHorizontalEmail']")))
# email_field.send_keys(f'{ReadConfigurations.get_config("panaray_prod_invalid_credentials", "invalid_email")}')
# driver.find_element(By.XPATH, "//input[@id='formHorizontalPassword']").send_keys(
#     f'{ReadConfigurations.get_config("panaray_prod_invalid_credentials", "invalid_password")}')
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# error_msg = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "//div[@class='errorMzs xx-small-normal']/child::strong[1]")))
# print(error_msg.text)
# print(error_msg.is_displayed())


def fake_email():
    email = Faker().email()
    return email


def fake_password():
    password = f"{Faker().name()}+!"
    return password

print(fake_email(),fake_password())
