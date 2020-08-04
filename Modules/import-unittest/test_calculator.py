# ###### Testing the calculator.py ######

# =================================
# Importing unittest module
import unittest

# Importing the file that we want to test
import calculator
# =================================
# ### Creating test cases ###

# We are inheriting from unittest.TestCase 
# Inheriting from unittest.TestCase will give us access to alot of testing capabilities within that class

class TestCalc(unittest.TestCase):

  # Method needs to start with test_ ,if this convention is not followed then we will not get error but no condition will be checked.
  # This naming convention is need in order to know which method represents test
  def test_add(self):
    result = calculator.add(10, 5)
    self.assertEqual(result, 15)

"""
The TestCase class provides several assert methods to check for and report failures. The following table lists the most commonly used methods (see the tables below for more assert methods):
Method                   | Checks that          | New in
------------------------------------------------------     
assertEqual(a, b)        | a == b               |
assertNotEqual(a, b)     | a != b               | 
assertTrue(x)            | bool(x) is True      |   
assertFalse(x)           | bool(x) is False     | 
assertIs(a, b)           | a is b               |   3.1
assertIsNot(a, b)        | a is not b           |   3.1
assertIsNone(x)          | x is None            |   3.1
assertIsNotNone(x)       | x is not None        |   3.1
assertIn(a, b)           | a in b               |   3.1
assertNotIn(a, b)        | a not in b           |   3.1
assertIsInstance(a, b)   | isinstance(a, b)     |   3.2
assertNotIsInstance(a, b)| not isinstance(a, b) |   3.2
"""
# =================================
# ### Running the test ###

# 1. From command line
# We cannot run the test just by ---> python test_calculator.py
# We have to run unittest as our main module and pass in test_calculator.py that is ---> python -m unittest test_calculator.py

# 2. To run our test directly
if __name__ == '__main__':
  unittest.main()

# Test success ---> . (you will get dot)
# Test fail ---> F
# =================================
# ### Creating class with more tests ###

class TestCalc(unittest.TestCase):

  def test_add(self):
    self.assertEqual(calculator.add(10, 5), 15)
    self.assertEqual(calculator.add(-1, 1), 0)
    self.assertEqual(calculator.add(-1, -1), -2)

    # It run's only one test since all the tests are under test_add
    # The goal is not to write as many as test you want but the goal is to write good test 

  def test_subtract(self):
    self.assertEqual(calculator.subtract(10, 5), 5)
    self.assertEqual(calculator.subtract(-1, 1), -2)
    self.assertEqual(calculator.subtract(-1, -1), 0)

  def test_multiply(self):
    self.assertEqual(calculator.multiply(10, 5), 50)
    self.assertEqual(calculator.multiply(-1, 1), -1)
    self.assertEqual(calculator.multiply(-1, -1), 1)

  def test_divide(self):
    self.assertEqual(calculator.divide(10, 5), 2)
    self.assertEqual(calculator.divide(-1, 1), -1)
    self.assertEqual(calculator.divide(-1, -1), 1)
  
    # It will give 4 . i.e. 4 Run

    # Sometimes we will make change that doesn't breaks our test but will break our code
    # Suppose we put --> x // y in divide function in our code, our test will not recoginze it since our results are whole number anyway which means our test is not broken but our code is surely broken

    # So it good to update your test with problems you find
    self.assertEqual(calculator.divide(5, 2), 2.5)
    # Now we will get AssertionError since 5 // 2 is not 2.5 but

    # To check our exception is working properly
    # There are two ways to do it:
    
    # 1.
    # First --> Exception 
    # Second --> Function we want to run but not passing the arguments, so not parenthese()
    # Third --> Pass each argument of function separatly
    # Reason to do this in this way rather than doing it normally is that our function will throw that ValueError and our test will think that something failed
    self.assertRaises(ValueError, calculator.divide, 10, 0)

    # If we put 2 instead of 0 then we will get an assertion error since ValueError was not raised
    self.assertRaises(ValueError, calculator.divide, 10, 2)

    # 2. 
    # This is not prfered, pass function normally is better way, this can be done by Context Manager
    with self.assertRaises(ValueError):
      calculator.divide(10, 0)

if __name__ == '__main__':
  unittest.main()
