# ###### Testing the employee.py ######

# =================================
# Test necessarily don't run in order, so never assume that the test runs straight down to the script therefore keep all the test isolated from one another

# Sometime it's also useful to run some code at the beinging of our test file and then have some cleanup code that runs after all of the tests runed
# So unlike setUp and tearDown that runs after and before every single test it would be nice if we have some that run once before anything and once after everything
# We can do this with two classmethods setUpClass and tearDownClass
# =================================
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    # This setUpClass and tearDownClass can be useful if we just want to do something once and it's too costly to do before each test
    # For example: We want to populate a database to run tests against as long as we're just reading from the database then it might be appropriate to just set this up once in the steUpClass method and then we can tear it down in the tearDownClass method

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

if __name__ == '__main__':
    unittest.main()
