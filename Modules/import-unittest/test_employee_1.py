# ###### Testing the employee.py ######

# =================================
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Brock', 'Lesnar', 50000)
        emp_2 = Employee('John', 'Cena', 60000)

        self.assertEqual(emp_1.email, 'Brock.Lesnar@email.com')
        self.assertEqual(emp_2.email, 'John.Cena@email.com')

        emp_1.first = 'Randy'
        emp_2.first = 'CM'

        self.assertEqual(emp_1.email, 'Randy.Lesnar@email.com')
        self.assertEqual(emp_2.email, 'CM.Cena@email.com')

    def test_fullname(self):
        emp_1 = Employee('Brock', 'Lesnar', 50000)
        emp_2 = Employee('John', 'Cena', 60000)

        self.assertEqual(emp_1.fullname, 'Brock Lesnar')
        self.assertEqual(emp_2.fullname, 'John Cena')

        emp_1.first = 'Randy'
        emp_2.first = 'CM'

        self.assertEqual(emp_1.fullname, 'John Lesnar')
        self.assertEqual(emp_2.fullname, 'CM Cena')

    def test_apply_raise(self):
        emp_1 = Employee('Brock', 'Lesnar', 50000)
        emp_2 = Employee('John', 'Cena', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)

if __name__ == '__main__':
    unittest.main()
# =================================
# Here we creating two employees again and again 
# But if we have to make changes then we go everywhere and make changes
# There is better way for this and that is to use setUp and tearDown methods
