import unittest


class MyUnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.my_set = {1, 2, 3, 5, 7}

    def test_set_discard(self):
        self.my_set.discard(3)
        self.assertEqual({1, 2, 5, 7}, self.my_set)

    def test_set_x_in_s(self):
        self.assertTrue(3 in self.my_set)
        self.assertFalse(4 in self.my_set)

    def test_set_add(self):
        self.assertTrue(12 not in self.my_set)
        self.my_set.add(12)
        self.assertTrue(12 in self.my_set)
