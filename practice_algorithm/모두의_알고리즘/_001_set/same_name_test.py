import unittest

from .same_name import find_same_name


class MySameNameTest(unittest.TestCase):
    def setUp(self) -> None:
        self.names = ['Tomcat', "Jetty", "Netty", "Undertow", "Netty"]

    def test_find_same_name(self):
        name_set = find_same_name(self.names)
        self.assertEqual({"Netty"}, name_set)

    def test_find_same_pop(self):
        self.names.pop(len(self.names) - 1)
        name = find_same_name(self.names)
        self.assertEqual(set(), name)
        self.assertTrue(len(name) == 0)
