from unittest import TestCase

from .trap import Solution


class TestSolution(TestCase):
    def test_trap(self):
        self.assertEqual(6, Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def test_stack(self):
        self.assertEqual(6, Solution().trap_stack([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
