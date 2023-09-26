from Pages.Login_Page import Login_Page
from Tests.Basetest import BaseTest


class TestPanarayLogin(BaseTest):
    def test_login_with_valid_credentials(self):
        login = Login_Page(self.driver)
        login.login_with_credentials(login.valid_email, login.valid_password)

    def test_login_with_invalid_credentials(self):
        login = Login_Page(self.driver)
        login.login_with_credentials(self.fake_email(), self.fake_password())
        login.display_error_msg()
        expected_error_msg = login.error_message
        login.assert_error_msg(expected_error_msg)

    def test_login_with_valid_email_and_invalid_password(self):
        login = Login_Page(self.driver)
        login.login_with_credentials(login.valid_email, self.fake_password())
        login.display_error_msg()
        expected_error_msg = login.error_message
        login.assert_error_msg(expected_error_msg)

    def test_login_with_invalid_email_and_valid_password(self):
        login = Login_Page(self.driver)
        login.login_with_credentials(self.fake_email(), login.valid_password)
        login.display_error_msg()
        expected_error_msg = login.error_message
        login.assert_error_msg(expected_error_msg)
