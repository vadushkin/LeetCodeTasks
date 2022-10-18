import unittest

import v1
import v2


class V1LongestUncommonSubsequenceTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v1.Solution()

        res1 = sol.findLUSlength("aaa", "bbb")
        res2 = sol.findLUSlength("aahage", "dbb")
        res3 = sol.findLUSlength("afffaaha", "bfbb")
        res4 = sol.findLUSlength("aaadsa", "bbgb")
        res5 = sol.findLUSlength("aaafd", "bbdsab")
        res6 = sol.findLUSlength("aaaaha", "ebhdabbad")
        res7 = sol.findLUSlength("afafsa", "bgbagahab")
        res8 = sol.findLUSlength("aahaa", "bggbgbaswd")
        res9 = sol.findLUSlength("aagaa", "bbggb")

        self.assertEqual(res1, 3)
        self.assertEqual(res2, 6)
        self.assertEqual(res3, 8)
        self.assertEqual(res4, 6)
        self.assertEqual(res5, 6)
        self.assertEqual(res6, 9)
        self.assertEqual(res7, 9)
        self.assertEqual(res8, 10)
        self.assertEqual(res9, 5)

    def test_failure_answers(self):
        sol = v1.Solution()

        res1 = sol.findLUSlength("aaa", "aaa")
        res2 = sol.findLUSlength("b", "b")
        res3 = sol.findLUSlength("TT", "TT")
        res4 = sol.findLUSlength("qw", "qw")
        res5 = sol.findLUSlength("aaafd", "aaafd")

        self.assertEqual(res1, -1)
        self.assertEqual(res2, -1)
        self.assertEqual(res3, -1)
        self.assertEqual(res4, -1)
        self.assertEqual(res5, -1)


class V2LongestUncommonSubsequenceTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v2.Solution()

        res1 = sol.findLUSlength("aaa", "bbb")
        res2 = sol.findLUSlength("aahage", "dbb")
        res3 = sol.findLUSlength("afffaaha", "bfbb")
        res4 = sol.findLUSlength("aaadsa", "bbgb")
        res5 = sol.findLUSlength("aaafd", "bbdsab")
        res6 = sol.findLUSlength("aaaaha", "ebhdabbad")
        res7 = sol.findLUSlength("afafsa", "bgbagahab")
        res8 = sol.findLUSlength("aahaa", "bggbgbaswd")
        res9 = sol.findLUSlength("aagaa", "bbggb")

        self.assertEqual(res1, 3)
        self.assertEqual(res2, 6)
        self.assertEqual(res3, 8)
        self.assertEqual(res4, 6)
        self.assertEqual(res5, 6)
        self.assertEqual(res6, 9)
        self.assertEqual(res7, 9)
        self.assertEqual(res8, 10)
        self.assertEqual(res9, 5)

    def test_failure_answers(self):
        sol = v2.Solution()

        res1 = sol.findLUSlength("aaa", "aaa")
        res2 = sol.findLUSlength("b", "b")
        res3 = sol.findLUSlength("TT", "TT")
        res4 = sol.findLUSlength("qw", "qw")
        res5 = sol.findLUSlength("aaafd", "aaafd")

        self.assertEqual(res1, -1)
        self.assertEqual(res2, -1)
        self.assertEqual(res3, -1)
        self.assertEqual(res4, -1)
        self.assertEqual(res5, -1)
