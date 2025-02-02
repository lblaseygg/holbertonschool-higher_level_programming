#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    
    def test_max_at_beginning(self):
        """Test with max integer at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
    
    def test_one_element_list(self):
        """Test with a list containing one element"""
        self.assertEqual(max_integer([7]), 7)
    
    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))
    
    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    
    def test_mixed_numbers(self):
        """Test with a mix of positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 3, 0, -2]), 5)
    
    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
    
    def test_mixed_ints_floats(self):
        """Test with a mix of integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.1]), 4.1)
    
    def test_large_numbers(self):
        """Test with very large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 500000]), 1000000)

if __name__ == "__main__":
    unittest.main()
