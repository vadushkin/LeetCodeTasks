import unittest

import v1
import v2
from v1 import TreeNode


class V1MinAbsoluteDifInBstTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v1.Solution()

        res1 = sol.getMinimumDifference(TreeNode(1, TreeNode(2)))
        res2 = sol.getMinimumDifference(TreeNode(1, TreeNode(2, TreeNode(3))))
        res3 = sol.getMinimumDifference(TreeNode(1, TreeNode(2, TreeNode(4))))
        res4 = sol.getMinimumDifference(TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(8)))))
        res5 = sol.getMinimumDifference(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(19))))
        res6 = sol.getMinimumDifference(TreeNode(1, TreeNode(2), TreeNode(1, TreeNode(2))))
        res7 = sol.getMinimumDifference(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(3, TreeNode(1)))))

        self.assertEqual(res1, -1)
        self.assertEqual(res2, -1)
        self.assertEqual(res3, -2)
        self.assertEqual(res4, -3)
        self.assertEqual(res5, -16)
        self.assertEqual(res6, -1)
        self.assertEqual(res7, -2)

    def test_failure_answers(self):
        sol = v1.Solution()

        res1 = sol.getMinimumDifference(TreeNode(1, TreeNode(2)))
        res2 = sol.getMinimumDifference(TreeNode(1, TreeNode(2, TreeNode(3))))
        res3 = sol.getMinimumDifference(TreeNode(1, TreeNode(2, TreeNode(4))))
        res4 = sol.getMinimumDifference(TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(8)))))
        res5 = sol.getMinimumDifference(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(19))))
        res6 = sol.getMinimumDifference(TreeNode(1, TreeNode(2), TreeNode(1, TreeNode(2))))
        res7 = sol.getMinimumDifference(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(3, TreeNode(1)))))

        self.assertTrue(res1 != 61)
        self.assertTrue(res2 != 4)
        self.assertTrue(res3 != 2)
        self.assertTrue(res4 != 5)
        self.assertTrue(res5 != 3)
        self.assertTrue(res6 != 1)
        self.assertTrue(res7 != 127)


class V2MinAbsoluteDifInBstTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v2.Solution()

        res1 = sol.getMinimumDifference(TreeNode(1, TreeNode(2)))
        res2 = sol.getMinimumDifference(TreeNode(1, TreeNode(2, TreeNode(3))))
        res3 = sol.getMinimumDifference(TreeNode(1, TreeNode(2, TreeNode(4))))
        res4 = sol.getMinimumDifference(TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(8)))))
        res5 = sol.getMinimumDifference(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(19))))
        res6 = sol.getMinimumDifference(TreeNode(1, TreeNode(2), TreeNode(1, TreeNode(2))))
        res7 = sol.getMinimumDifference(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(3, TreeNode(1)))))

        self.assertEqual(res1, -1)
        self.assertEqual(res2, -1)
        self.assertEqual(res3, -2)
        self.assertEqual(res4, -3)
        self.assertEqual(res5, -16)
        self.assertEqual(res6, -1)
        self.assertEqual(res7, -2)

    def test_failure_answers(self):
        sol = v2.Solution()

        res1 = sol.getMinimumDifference(TreeNode(1, TreeNode(2)))
        res2 = sol.getMinimumDifference(TreeNode(1, TreeNode(2, TreeNode(3))))
        res3 = sol.getMinimumDifference(TreeNode(1, TreeNode(2, TreeNode(4))))
        res4 = sol.getMinimumDifference(TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(8)))))
        res5 = sol.getMinimumDifference(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(19))))
        res6 = sol.getMinimumDifference(TreeNode(1, TreeNode(2), TreeNode(1, TreeNode(2))))
        res7 = sol.getMinimumDifference(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(3, TreeNode(1)))))

        self.assertTrue(res1 != 61)
        self.assertTrue(res2 != 4)
        self.assertTrue(res3 != 2)
        self.assertTrue(res4 != 5)
        self.assertTrue(res5 != 3)
        self.assertTrue(res6 != 1)
        self.assertTrue(res7 != 127)
