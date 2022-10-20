import unittest

import v1
import v2


class TwoSumTestCase(unittest.TestCase):
    def test_correct_results(self):
        sol = v1.Solution()

        res1 = sol.twoSum([1, 2, 3, 4, 5, 6, 7, 8], 10)
        res2 = sol.twoSum([1, 6, 7, 8], 7)
        res3 = sol.twoSum([10, 5, 3, 4, 35, 6, 7, 8], 45)
        res4 = sol.twoSum([1, 2, 3, 4, 5, 6, 7, 17], 5)
        res5 = sol.twoSum([7, 8, 5], 15)
        res6 = sol.twoSum([1, 2], 2)
        res7 = sol.twoSum([2, 3, 4, 100], 7)
        res8 = sol.twoSum([1, 2, 3, 4, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 25)
        res9 = sol.twoSum([10, 45, 14, 71, 51, 155, 16], 10)
        res10 = sol.twoSum([0, 1, 0], 1)

        self.assertEqual(res1, [1, 7])
        self.assertEqual(res2, [0, 1])
        self.assertEqual(res3, [0, 4])
        self.assertEqual(res4, [0, 3])
        self.assertEqual(res5, [0, 1])
        self.assertEqual(res6, None)
        self.assertEqual(res7, [1, 2])
        self.assertEqual(res8, [7, 16])
        self.assertEqual(res9, None)
        self.assertEqual(res10, [0, 1])

    def test_wrong_results(self):
        sol = v1.Solution()

        res1 = sol.twoSum([1, 2, 3, 4, 5, 6, 7, 8], 9)
        res2 = sol.twoSum([1, 6, 7, 8], 8)
        res3 = sol.twoSum([10, 2, 3, 4, 35, 6, 7, 8], 44)
        res4 = sol.twoSum([1, 2, 3, 4, 5, 6, 7, 8], 1)
        res5 = sol.twoSum([7, 8], 8)
        res6 = sol.twoSum([1, 2], 4)
        res7 = sol.twoSum([2, 3, 4], 71)
        res8 = sol.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 55)
        res9 = sol.twoSum([10, 45, 14, 71, 51, 155, 13], 70)
        res10 = sol.twoSum([0, 1], 5)

        self.assertTrue(res1 != [1, 7])
        self.assertTrue(res2 != [0, 1])
        self.assertTrue(res3 != [0, 4])
        self.assertTrue(res4 != [0, 3])
        self.assertTrue(res5 != [0, 1])
        self.assertTrue(res6 is None)
        self.assertTrue(res7 != [1, 2])
        self.assertTrue(res8 != [7, 16])
        self.assertTrue(res9 is None)
        self.assertTrue(res10 != [0, 1])

    def test_empty_values(self):
        sol = v1.Solution()
        res1 = sol.twoSum([], 1)
        res2 = sol.twoSum([1], 5)
        res3 = sol.twoSum([1, 4], 2)
        res4 = sol.twoSum([1000000000000000], 1000000000000000)
        res5 = sol.twoSum([-1000000000000000], -1000000000000000)
        res6 = sol.twoSum([1, 2, 3, 4], 10000000000000000000)
        res7 = sol.twoSum([100000000000000], 4)

        self.assertEqual(res1, None)
        self.assertEqual(res2, None)
        self.assertEqual(res3, None)
        self.assertEqual(res4, None)
        self.assertEqual(res5, None)
        self.assertEqual(res5, None)
        self.assertEqual(res6, None)
        self.assertEqual(res7, None)


class V2TwoSumTestCase(unittest.TestCase):
    def test_correct_results(self):
        sol = v2.Solution()

        res1 = sol.twoSum([1, 2, 3, 4, 5, 6, 7, 8], 10)
        res2 = sol.twoSum([1, 6, 7, 8], 7)
        res3 = sol.twoSum([10, 2, 3, 4, 35, 6, 7, 8], 45)
        res4 = sol.twoSum([1, 2, 3, 4, 5, 6, 7, 8], 5)
        res5 = sol.twoSum([7, 8], 15)
        res6 = sol.twoSum([1, 2], 2)
        res7 = sol.twoSum([2, 3, 4], 7)
        res8 = sol.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 25)
        res9 = sol.twoSum([10, 45, 14, 71, 51, 155, 13], 10)
        res10 = sol.twoSum([0, 1], 1)

        self.assertEqual(res1, [3, 5])
        self.assertEqual(res2, [0, 1])
        self.assertEqual(res3, [0, 4])
        self.assertEqual(res4, [0, 3])
        self.assertEqual(res5, [0, 1])
        self.assertEqual(res6, None)
        self.assertEqual(res7, [0, 3])
        self.assertEqual(res8, [7, 16])
        self.assertEqual(res9, None)
        self.assertEqual(res10, [0, 1])

    def test_wrong_results(self):
        sol = v2.Solution()

        res1 = sol.twoSum([1, 2, 3, 4, 5, 6, 7, 8], 9)
        res2 = sol.twoSum([1, 6, 7, 8], 8)
        res3 = sol.twoSum([10, 2, 3, 4, 35, 6, 7, 8], 44)
        res4 = sol.twoSum([1, 2, 3, 4, 5, 6, 7, 8], 1)
        res5 = sol.twoSum([7, 8], 8)
        res6 = sol.twoSum([1, 2], 4)
        res7 = sol.twoSum([2, 3, 4], 71)
        res8 = sol.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 55)
        res9 = sol.twoSum([10, 45, 14, 71, 51, 155, 13], 70)
        res10 = sol.twoSum([0, 1], 5)

        self.assertTrue(res1 != [1, 7])
        self.assertTrue(res2 != [0, 1])
        self.assertTrue(res3 != [0, 4])
        self.assertTrue(res4 != [0, 3])
        self.assertTrue(res5 != [0, 1])
        self.assertTrue(res6 is None)
        self.assertTrue(res7 != [0, 3])
        self.assertTrue(res8 != [7, 16])
        self.assertTrue(res9 is None)
        self.assertTrue(res10 != [0, 1])

    def test_empty_values(self):
        sol = v2.Solution()

        res1 = sol.twoSum([], 1)
        res2 = sol.twoSum([1], 5)
        res3 = sol.twoSum([1, 4], 2)
        res4 = sol.twoSum([1000000053200000], 1000000000000000)
        res5 = sol.twoSum([-1000000000000000], -10000000000300000)
        res6 = sol.twoSum([1, 2, 3, 4], 10000000000000000000)
        res7 = sol.twoSum([100000005000000], 4)

        self.assertEqual(res1, None)
        self.assertEqual(res2, None)
        self.assertEqual(res3, None)
        self.assertEqual(res4, None)
        self.assertEqual(res5, None)
        self.assertEqual(res5, None)
        self.assertEqual(res6, None)
        self.assertEqual(res7, None)
