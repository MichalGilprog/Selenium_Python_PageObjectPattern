from selenium.webdriver.common.by import By
import pytest
import random
from pages.my_account_page import MyAccountPage
from pages.billing_address_page import BillingAddressPage


@pytest.mark.usefixtures('setup')
class TestUpdateBillingAddress:

    def test_update_billing_address_passed(self):
        email = str(random.randint(0, 10000)) + 'nowekonto@gmail.com'
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, 'nowekonto1234')
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("John", "Weak")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address('Kwiatkowskiego 1', '01-001', 'Warsaw')
        billing_address_page.set_phone('123456789')
        billing_address_page.save_address()
        msg = 'Address changed successfully'
        assert msg in billing_address_page.get_message_text()
