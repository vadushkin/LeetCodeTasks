import unittest

import v1
import v2


class V1SetMismatchTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v1.Solution()

        res1 = sol.findErrorNums([1, 2, 3, 4, 4, 6])
        res2 = sol.findErrorNums([1, 1])
        res3 = sol.findErrorNums([1, 3, 4, 4, 5])
        res4 = sol.findErrorNums([1, 2, 3, 3])
        res5 = sol.findErrorNums([1, 2, 2])
        res6 = sol.findErrorNums([1, 3, 4, 2, 4, 5])
        res7 = sol.findErrorNums([1, 2, 3, 1])
        res8 = sol.findErrorNums([1, 4, 2, 3, 6, 4])
        res9 = sol.findErrorNums([5, 2, 1, 4, 3, 5])
        res10 = sol.findErrorNums([1, 2, 3, 5, 3])

        self.assertEqual(res1, [4, 5])
        self.assertEqual(res2, [1, 2])
        self.assertEqual(res3, [4, 2])
        self.assertEqual(res4, [3, 4])
        self.assertEqual(res5, [2, 3])
        self.assertEqual(res6, [4, 6])
        self.assertEqual(res7, [1, 4])
        self.assertEqual(res8, [4, 5])
        self.assertEqual(res9, [5, 6])
        self.assertEqual(res10, [3, 4])


class V2SetMismatchTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v2.Solution()

        res1 = sol.findErrorNums([1, 2, 3, 4, 4, 6])
        res2 = sol.findErrorNums([1, 1])
        res3 = sol.findErrorNums([1, 3, 4, 4, 5])
        res4 = sol.findErrorNums([1, 2, 3, 3])
        res5 = sol.findErrorNums([1, 2, 2])
        res6 = sol.findErrorNums([1, 3, 4, 2, 4, 5])
        res7 = sol.findErrorNums([1, 2, 3, 1])
        res8 = sol.findErrorNums([1, 4, 2, 3, 6, 4])
        res9 = sol.findErrorNums([5, 2, 1, 4, 3, 5])
        res10 = sol.findErrorNums([1, 2, 3, 5, 3])

        self.assertEqual(res1, [4, 5])
        self.assertEqual(res2, [1, 2])
        self.assertEqual(res3, [4, 2])
        self.assertEqual(res4, [3, 4])
        self.assertEqual(res5, [2, 3])
        self.assertEqual(res6, [4, 6])
        self.assertEqual(res7, [1, 4])
        self.assertEqual(res8, [4, 5])
        self.assertEqual(res9, [5, 6])
        self.assertEqual(res10, [3, 4])
