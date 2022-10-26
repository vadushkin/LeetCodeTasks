import unittest

import v1
import v2


class V1ContinuousSubarraySumTestCase(unittest.TestCase):
    def test_true_answers(self):
        sol = v1.Solution()

        res1 = sol.checkSubarraySum([1, 2, 3], 5)
        res2 = sol.checkSubarraySum([23, 2, 6, 4, 7], 6)
        res3 = sol.checkSubarraySum([23, 2, 4, 6, 7], 6)
        res4 = sol.checkSubarraySum([1, 2, 3, 4], 10)
        res5 = sol.checkSubarraySum([1, 2], 3)

        self.assertTrue(res1)
        self.assertTrue(res2)
        self.assertTrue(res3)
        self.assertTrue(res4)
        self.assertTrue(res5)

    def test_false_answers(self):
        sol = v1.Solution()

        res1 = sol.checkSubarraySum([23, 2, 6, 4, 7], 0)
        res2 = sol.checkSubarraySum([1, 1, 1], 4)
        res3 = sol.checkSubarraySum([1, 2, 3, 4], 11)
        res4 = sol.checkSubarraySum([], 0)
        res5 = sol.checkSubarraySum([1], 1)

        self.assertFalse(res1)
        self.assertFalse(res2)
        self.assertFalse(res3)
        self.assertFalse(res4)
        self.assertFalse(res5)


class V2ContinuousSubarraySumTestCase(unittest.TestCase):
    def test_true_answers(self):
        sol = v2.Solution()

        res1 = sol.checkSubarraySum([1, 2, 3], 5)
        res2 = sol.checkSubarraySum([23, 2, 6, 4, 7], 6)
        res3 = sol.checkSubarraySum([23, 2, 4, 6, 7], 6)
        res4 = sol.checkSubarraySum([1, 2, 3, 4], 10)
        res5 = sol.checkSubarraySum([1, 2], 3)

        self.assertTrue(res1)
        self.assertTrue(res2)
        self.assertTrue(res3)
        self.assertTrue(res4)
        self.assertTrue(res5)

    def test_false_answers(self):
        sol = v2.Solution()

        res1 = sol.checkSubarraySum([23, 2, 6, 4, 7], 0)
        res2 = sol.checkSubarraySum([1, 1, 1], 4)
        res3 = sol.checkSubarraySum([1, 2, 3, 4], 11)
        res4 = sol.checkSubarraySum([], 0)
        res5 = sol.checkSubarraySum([1], 1)

        self.assertFalse(res1)
        self.assertFalse(res2)
        self.assertFalse(res3)
        self.assertFalse(res4)
        self.assertFalse(res5)
