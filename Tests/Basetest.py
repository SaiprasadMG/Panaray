import pytest
from faker import Faker


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class BaseTest:
    def fake_email(self):
        email = Faker().email()
        return email

    def fake_password(self):
        password = f"{Faker().name()}+!"
        return password
