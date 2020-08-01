import unittest
from .same_name import find_same_name


class MySameNameTest(unittest.TestCase):
    def test_find_same_name(self):
        names = ['Tomcat', "Jetty", "Netty", "Undertow", "Netty"]
        name_set = find_same_name(names)
        self.assertEqual({"Netty"}, name_set)
