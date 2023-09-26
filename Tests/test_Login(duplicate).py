import pytest

from Pages.Login_Page import Login_Page
from Tests.Basetest import BaseTest
from Utilities import ExcelUtils


class TestPanarayLoginDuplicate(BaseTest):
    @pytest.mark.parametrize("email,password",ExcelUtils.get_data_from_excel("ExcelFiles/Excelfile.xlsx","Login"))
    def test_login_with_valid_credentials_Duplicate(self,email,password):
        login = Login_Page(self.driver)
        login.login_with_credentials(email, password)

    def test_login_with_invalid_credentials_Duplicate(self):
        login = Login_Page(self.driver)
        login.login_with_credentials(self.fake_email(), self.fake_password())
        login.display_error_msg()
        expected_error_msg = login.error_message
        login.assert_error_msg(expected_error_msg)

    def test_login_with_valid_email_and_invalid_password_Duplicate(self):
        login = Login_Page(self.driver)
        login.login_with_credentials(login.valid_email, self.fake_password())
        login.display_error_msg()
        expected_error_msg = login.error_message
        login.assert_error_msg(expected_error_msg)

    def test_login_with_invalid_email_and_valid_password_Duplicate(self):
        login = Login_Page(self.driver)
        login.login_with_credentials(self.fake_email(), login.valid_password)
        login.display_error_msg()
        expected_error_msg = login.error_message
        login.assert_error_msg(expected_error_msg)
