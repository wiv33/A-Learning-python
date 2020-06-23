import unittest


class FirstTestMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), "FOO")

    def test_is_upper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        world = 'hello world'
        self.assertEqual(world.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            world.split(2)


if __name__ == '__main__':
    unittest.main()
