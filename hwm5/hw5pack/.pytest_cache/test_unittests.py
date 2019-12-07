import unittest
from hw5pack import divisor_master as dm


class TestDivisorMaster(unittest.TestCase):
    def test_is_simple_true(self):
       self.assertTrue(dm.is_simple(17))

    def test_is_simple_false(self):
        self.assertFalse(dm.is_simple(24))

    def test__get_dividers(self):
        num_in = 34
        test_list = [1, 2, 17, 34]
        self.assertEqual(dm._get_dividers(num_in), test_list)

    def test__get_all_simple_dividers(self):
        list_in = [1, 2, 4, 17, 24]
        list_out = [2, 17]
        self.assertEqual(dm._get_all_simple_dividers(list_in), list_out)

    def test_max_simple_divider(self):
        self.assertEqual(dm.max_simple_divider(34), 17)