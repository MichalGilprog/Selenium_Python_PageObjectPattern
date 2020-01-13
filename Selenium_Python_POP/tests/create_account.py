from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import random
import pytest

from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures('setup')
class TestCreateAccount:

    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account('nowekonto@gmail.com', 'To jest nowe haslo')

        msg = 'Error: An account is already registered with your email address. Please log in.'
        assert msg in my_account_page.get_error_msg()

    def test_create_account_passed(self):
        email = str(random.randint(0, 10000)) + 'nowekonto@gmail.com'
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, 'To jest nowe haslo')

        assert my_account_page.is_logout_link_displayed()



