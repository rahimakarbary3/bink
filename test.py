import unittest
import bink_q1
import bink_q2
import bink_q3
import bink_q4

class TestQuestion1(unittest.TestCase):
    def test_current_rent(self):
        """
        Test that it extracts the correct number of list items
        """
        result = bink_q1.RentExtract()
        expected = 5
        self.assertEqual(expected, result)

class TestQuestion2(unittest.TestCase):
    def test_rent_total(self):
        """
        Test that the total rent is correct
        """
        result = bink_q2.LeaseYear()
        expected = 46500
        self.assertEqual(expected, result)

class TestQuestion3(unittest.TestCase):
    def test_mast_total(self):
        """
        Test that the total number of mast is correct
        """
        result = bink_q3.TotalMast()
        expected = 42
        self.assertEqual(expected, result)

class TestQuestion4(unittest.TestCase):
    def test_lease_total(self):
        """
        Test that the total number of outputted lines is correct
        """
        result = bink_q4.TotalLease()
        expected = 5
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()