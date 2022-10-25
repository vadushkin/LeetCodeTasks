import unittest

import v1
import v2


class V1CheckIfTwoStringArraysAreEquivalentTestCase(unittest.TestCase):
    def test_true_answers(self):
        sol = v1.Solution()

        res1 = sol.arrayStringsAreEqual(["ab", "c"], ["a", "bc"])
        res2 = sol.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"])
        res3 = sol.arrayStringsAreEqual(["a", "q"], ["aq"])
        res4 = sol.arrayStringsAreEqual(["asdfasdfasdf"], ["asdfasdfasdf"])
        res5 = sol.arrayStringsAreEqual(["amo", "oma", "amo"], ["amo", "omaamo"])

        self.assertTrue(res1)
        self.assertTrue(res2)
        self.assertTrue(res3)
        self.assertTrue(res4)
        self.assertTrue(res5)

    def test_false_answers(self):
        sol = v1.Solution()

        res1 = sol.arrayStringsAreEqual(["ab", "c"], ["a", "cc"])
        res2 = sol.arrayStringsAreEqual(['as', 'sa'], ['aass'])
        res3 = sol.arrayStringsAreEqual(['qwerty', 'qwe'], ['qweqwerty'])
        res4 = sol.arrayStringsAreEqual(['fff', 'ff'], ['ffffff'])
        res5 = sol.arrayStringsAreEqual(['e'], ['ee'])

        self.assertFalse(res1)
        self.assertFalse(res2)
        self.assertFalse(res3)
        self.assertFalse(res4)
        self.assertFalse(res5)


class V2CheckIfTwoStringArraysAreEquivalentTestCase(unittest.TestCase):
    def test_true_answers(self):
        sol = v2.Solution()

        res1 = sol.arrayStringsAreEqual(["ab", "c"], ["a", "bc"])
        res2 = sol.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"])
        res3 = sol.arrayStringsAreEqual(["a", "q"], ["aq"])
        res4 = sol.arrayStringsAreEqual(["asdfasdfasdf"], ["asdfasdfasdf"])
        res5 = sol.arrayStringsAreEqual(["amo", "oma", "amo"], ["amo", "omaamo"])

        self.assertTrue(res1)
        self.assertTrue(res2)
        self.assertTrue(res3)
        self.assertTrue(res4)
        self.assertTrue(res5)

    def test_false_answers(self):
        sol = v2.Solution()

        res1 = sol.arrayStringsAreEqual(["ab", "c"], ["a", "cc"])
        res2 = sol.arrayStringsAreEqual(['as', 'sa'], ['aass'])
        res3 = sol.arrayStringsAreEqual(['qwerty', 'qwe'], ['qweqwerty'])
        res4 = sol.arrayStringsAreEqual(['fff', 'ff'], ['ffffff'])
        res5 = sol.arrayStringsAreEqual(['e'], ['ee'])

        self.assertFalse(res1)
        self.assertFalse(res2)
        self.assertFalse(res3)
        self.assertFalse(res4)
        self.assertFalse(res5)
