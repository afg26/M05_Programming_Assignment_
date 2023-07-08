#Ahmad Ghaznawi
#importing the test runner for our app.
import unittest
#importing the Fraction module for failing one of the tests
from fractions import Fraction

#importing the sum function from my_sum which takes an iterable (a list, tuple, or set) and adds the values together.
from my_sum import sum

# Defining a new test case class called TestSum, which inherits from unittest.TestCase
class TestSum(unittest.TestCase):

    """
    Defining a test method to test a list of integers.
    Test that it can sum a list of integers
    """
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


    def test_list_fraction(self):
        """
        Defining a test method to test a list of fractions
        This test is going to fail
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

#Defining a command-line entry point, which runs the unittest test-runner
if __name__ == '__main__':
    unittest.main()


"""
The unit testing is one of best aspect that a programmer must have in his code, while he runs his code even multiple
times, still you can find some minor mistakes and problems.
this unit test that I have created is going to sum a list of integers on the first part and the second function is 
going to test a list of fractions because we made this function in a way that it is going to fail.
"""