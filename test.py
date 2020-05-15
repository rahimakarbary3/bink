import unittest
import bink_q1


class TestRentExtract(unittest.TestCase):
    def test_current_rent(self):
        """
        Test that it extracts the correct number of list items
        """
        result = bink_q1.RentExtract()
        expected = 5
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()