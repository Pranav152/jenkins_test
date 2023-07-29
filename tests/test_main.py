"""Script to test the add function."""

import unittest
from main import add

# This is a class to test the add function
class TestAddFunctionTestCase(unittest.TestCase):
    """Test cases for the add function."""
    def test_add(self):
        """Test the add function with two numbers."""
        self.assertEqual(add(2, 3), 5)
