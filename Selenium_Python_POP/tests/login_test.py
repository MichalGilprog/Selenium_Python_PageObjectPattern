from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

from pages.my_account_page import MyAccountPage
import pytest


@pytest.mark.usefixtures('setup')
class TestLogIn:

    def test_log_in_passed(self):
        log_in_passed = MyAccountPage(self.driver)
        log_in_passed.open_page()
        log_in_passed.log_in("dwa2@dwa.com", "Ala ma kota")

        assert log_in_passed.is_logout_link_displayed()

    def test_log_in_failed(self):
        log_in_failed = MyAccountPage(self.driver)
        log_in_failed.open_page()
        log_in_failed.log_in("dwa2@dwa.com1", "Ala ma kota1")

        msg = "ERROR: Incorrect username or password."
        assert msg in log_in_failed.get_error_msg()

# time.sleep(4)
