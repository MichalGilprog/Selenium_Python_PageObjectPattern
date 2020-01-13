# SeleniumPyProject_Page Object Pattern


Project: Seleniumdemo.com

I. Test procedure specification: New user registration

Preconditions:
1. Browser open on the page: http://seleniumdemo.com/

Steps:
1. Click on "My account"
2. Enter email address in Register section
3. Enter password in Registration section
4. Press "REGISTER" button
5. Check the correctness of displayed messages


II. Test procedure specification: New user registration plus update billing address

Preconditions:
1. Browser open on the page: http://seleniumdemo.com/?page_id=7

Steps:

1. Enter email address in Register section
2. Enter password in Registration section
3. Press "REGISTER" button
4. Press "Addresses" button
5. Press "Edit" button next to "Billing address"
6. Set First name
7. Set Last name
8. Select Country
9. Set Street address
10. Set Postcode
11. Set Town/City
12. Set Phone number
13. Press "SAVE ADDRESS" button
14. Check the correctness of displayed messages
