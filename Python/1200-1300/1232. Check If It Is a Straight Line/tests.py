import unittest

import v1
import v2


class V1CheckStraightLineTestCase(unittest.TestCase):
    def test_true_answers(self):
        sol = v1.Solution()

        res1 = sol.checkStraightLine([[1, 2], [2, 3], [3, 4]])
        res2 = sol.checkStraightLine([[1, 1], [2, 2], [3, 3], [4, 4]])
        res3 = sol.checkStraightLine([[1, 1], [11, 11]])
        res4 = sol.checkStraightLine([[0, 0], [10, 10]])
        res5 = sol.checkStraightLine([[50, 20], [100, 40], [150, 60]])

        self.assertTrue(res1)
        self.assertTrue(res2)
        self.assertTrue(res3)
        self.assertTrue(res4)
        self.assertTrue(res5)

    def test_false_answers(self):
        sol = v1.Solution()

        res1 = sol.checkStraightLine([[1, 2], [5, 3], [3, 4]])
        res2 = sol.checkStraightLine([[1, 1], [4, 2], [3, 3], [4, 4]])
        res3 = sol.checkStraightLine([[1, 2], [15, 20], [4, 2]])
        res4 = sol.checkStraightLine([[0, 1], [10, 151], [3, 1]])
        res5 = sol.checkStraightLine([[1, 1], [2, 3], [4, 5]])
        res6 = sol.checkStraightLine([[5, 6], [5, 1], [1, 1]])
        res7 = sol.checkStraightLine([[50, 20], [100, 41], [31, 2]])

        self.assertFalse(res1)
        self.assertFalse(res2)
        self.assertFalse(res3)
        self.assertFalse(res4)
        self.assertFalse(res5)
        self.assertFalse(res6)
        self.assertFalse(res7)


class V2CheckStraightLineTestCase(unittest.TestCase):
    def test_true_answers(self):
        sol = v2.Solution()

        res1 = sol.checkStraightLine([[1, 2], [2, 3], [3, 4]])
        res2 = sol.checkStraightLine([[1, 1], [2, 2], [3, 3], [4, 4]])
        res3 = sol.checkStraightLine([[1, 1], [11, 11]])
        res4 = sol.checkStraightLine([[0, 0], [10, 10]])
        res5 = sol.checkStraightLine([[50, 20], [100, 40], [150, 60]])

        self.assertTrue(res1)
        self.assertTrue(res2)
        self.assertTrue(res3)
        self.assertTrue(res4)
        self.assertTrue(res5)

    def test_false_answers(self):
        sol = v2.Solution()

        res1 = sol.checkStraightLine([[1, 2], [5, 3], [3, 4]])
        res2 = sol.checkStraightLine([[1, 1], [4, 2], [3, 3], [4, 4]])
        res3 = sol.checkStraightLine([[1, 2], [15, 20], [4, 2]])
        res4 = sol.checkStraightLine([[0, 1], [10, 151], [3, 1]])
        res5 = sol.checkStraightLine([[1, 1], [2, 3], [4, 5]])
        res6 = sol.checkStraightLine([[5, 6], [5, 1], [1, 1]])
        res7 = sol.checkStraightLine([[50, 20], [100, 41], [31, 2]])

        self.assertFalse(res1)
        self.assertFalse(res2)
        self.assertFalse(res3)
        self.assertFalse(res4)
        self.assertFalse(res5)
        self.assertFalse(res6)
        self.assertFalse(res7)
