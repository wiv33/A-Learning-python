from unittest import TestCase

from .reorder_log_files import reorder_log_files


class TestReorderLogFiles(TestCase):
    def setUp(self) -> None:
        self.logs = ["dig1 8 1 5 1",
                     "let1 art can",
                     'dig2 3 6',
                     'let2 own kit dig',
                     'let3 art zero']
        self.expected = ["let1 art can",
                         "let3 art zero",
                         'let2 own kit dig',
                         'dig1 8 1 5 1',
                         'dig2 3 6']

    def test_reorder_log_files(self):
        files = reorder_log_files(self.logs)
        self.assertEqual(self.expected, files)
