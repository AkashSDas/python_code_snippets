# ###### Testing the employee.py ######

# =================================
# Sometimes our code relies on certain things that we have no control over
# Example: We have a function that goes to a website and pulls down some information, now if that website is down then your function is going to fail which also make your test fail but this isn't what we want because we only want our test to fail if somthing is wrong with our code 
# So if a website is down then there's nothing that we can actually do about that so we're going to get around this with something called mocking 
# We are just going to look at Basic Usage of mocking 
# =================================
import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Brock', 'Lesnar', 50000)
        self.emp_2 = Employee('John', 'Cena', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Brock.Lesnar@email.com') 
        self.assertEqual(self.emp_2.email, 'John.Cena@email.com')

        self.emp_1.first = 'Randy'
        self.emp_2.first = 'CM'

        self.assertEqual(self.emp_1.email, 'Randy.Lesnar@email.com')
        self.assertEqual(self.emp_2.email, 'CM.Cena@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Brock Lesnar')
        self.assertEqual(self.emp_2.fullname, 'John Cena')

        self.emp_1.first = 'Randy'
        self.emp_2.first = 'CM'

        self.assertEqual(self.emp_1.fullname, 'Randy Lesnar')
        self.assertEqual(self.emp_2.fullname, 'CM Cena')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    # We are just concernced with the get request was called with correct URL and that our code behaves correctly whether the response is okay or whether the response is not okay

    # There are multiple ways we can use patch, we can use patch either as a decprator or as a context manager and it will allow us to mock an object during a test and then that object is automatically restored after the is run

    def test_monthly_schedule(self):
      # Using patch as context manager
      # Within patch we passed what we want to mock request.get of the employee module and then we are setting that equal to mocked_get
      # If we wonder why didn't we import request module into our test and just mock that insead of the employee requestbut we want to mock these objects where they're actually used in this employee module
      with patch('employee.requests.get') as mocked_get:

        # To check a sucessfull call
        mocked_get.return_value.ok = True
        mocked_get.return_value.text = 'Success'

        schedule = self.emp_1.monthly_schedule('May')
        # One thing of mock object is that they record when they were called and with what values
        # To make sure that the get method was called with the correct URL
        mocked_get.asset_called_with('http://company.com/Lesnar/May')
        self.assertEqual(schedule, 'Success')

        # To check a fail reaponse
        mocked_get.return_value.ok = False
        schedule = self.emp_1.monthly_schedule('June')
        mocked_get.asset_called_with('http://company.com/Cena/June')
        self.assertEqual(schedule, 'Bad Response!')

# We will not use mocking unless we are testing something that is out of our control

if __name__ == '__main__':
    unittest.main()
