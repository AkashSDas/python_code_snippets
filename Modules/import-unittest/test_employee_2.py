# ###### Testing the employee.py ######

# =================================
# ### Using setUp and tearDown methods ###

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    # setUp code will run before every single test
    def setUp(self):
      self.emp_1 = Employee('Brock', 'Lesnar', 50000)
      self.emp_2 = Employee('John', 'Cena', 60000)

    # tearDown code will run after every single test
    # It can be used in case such that if we have functions that we want to test that added files in directories/databeses
    def tearDown(self):
      pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Brock.Lesnar@email.com')
        self.assertEqual(self.emp_2.email, 'John.Cena@email.com')

        self.emp_1.first = 'Randy'
        self.emp_2.first = 'CM'

        self.assertEqual(self.emp_1.email, 'Randy.Lesnar@email.com')
        self.assertEqual(self.emp_2.email, 'CM.Cena@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Brock Lesnar')
        self.assertEqual(self.emp_2.fullname, 'John Cena')

        self.emp_1.first = 'Randy'
        self.emp_2.first = 'CM'

        self.assertEqual(self.emp_1.fullname, 'John Lesnar')
        self.assertEqual(self.emp_2.fullname, 'CM Cena')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

if __name__ == '__main__':
    unittest.main()    
