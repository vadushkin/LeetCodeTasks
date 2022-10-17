import unittest

import v1
import v2


class V1DetectCapitalTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v1.Solution()

        res1 = sol.detectCapitalUse("USA")
        res2 = sol.detectCapitalUse("AMERICA")
        res3 = sol.detectCapitalUse("Hello")
        res4 = sol.detectCapitalUse("Capital")
        res5 = sol.detectCapitalUse("leetcode")
        res6 = sol.detectCapitalUse("leeeeee")
        res7 = sol.detectCapitalUse("UA")
        res8 = sol.detectCapitalUse("ohao")
        res9 = sol.detectCapitalUse("broken")

        self.assertEqual(res1, True)
        self.assertEqual(res2, True)
        self.assertEqual(res3, True)
        self.assertEqual(res4, True)
        self.assertEqual(res5, True)
        self.assertEqual(res6, True)
        self.assertEqual(res7, True)
        self.assertEqual(res8, True)
        self.assertEqual(res9, True)

    def test_failure_answers(self):
        sol = v1.Solution()

        res1 = sol.detectCapitalUse("NORTh")
        res2 = sol.detectCapitalUse("CooleR")
        res3 = sol.detectCapitalUse("anS")
        res4 = sol.detectCapitalUse("WHAt")
        res5 = sol.detectCapitalUse("leetcodE")
        res6 = sol.detectCapitalUse("HEllo")
        res7 = sol.detectCapitalUse("BROKEn")
        res8 = sol.detectCapitalUse("WREATh")
        res9 = sol.detectCapitalUse("pC")

        self.assertEqual(res1, False)
        self.assertEqual(res2, False)
        self.assertEqual(res3, False)
        self.assertEqual(res4, False)
        self.assertEqual(res5, False)
        self.assertEqual(res6, False)
        self.assertEqual(res7, False)
        self.assertEqual(res8, False)
        self.assertEqual(res9, False)


class V2DetectCapitalTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v2.Solution()

        res1 = sol.detectCapitalUse("USA")
        res2 = sol.detectCapitalUse("AMERICA")
        res3 = sol.detectCapitalUse("Hello")
        res4 = sol.detectCapitalUse("Capital")
        res5 = sol.detectCapitalUse("leetcode")
        res6 = sol.detectCapitalUse("myau")
        res7 = sol.detectCapitalUse("haf")
        res8 = sol.detectCapitalUse("hamburger")
        res9 = sol.detectCapitalUse("broke")

        self.assertEqual(res1, True)
        self.assertEqual(res2, True)
        self.assertEqual(res3, True)
        self.assertEqual(res4, True)
        self.assertEqual(res5, True)
        self.assertEqual(res6, True)
        self.assertEqual(res7, True)
        self.assertEqual(res8, True)
        self.assertEqual(res9, True)

    def test_failure_answers(self):
        sol = v2.Solution()

        res1 = sol.detectCapitalUse("NORTh")
        res2 = sol.detectCapitalUse("CooleR")
        res3 = sol.detectCapitalUse("anS")
        res4 = sol.detectCapitalUse("WHAt")
        res5 = sol.detectCapitalUse("leetcodE")
        res6 = sol.detectCapitalUse("HEllo")
        res7 = sol.detectCapitalUse("BROKEn")
        res8 = sol.detectCapitalUse("WREATh")
        res9 = sol.detectCapitalUse("pC")

        self.assertEqual(res1, False)
        self.assertEqual(res2, False)
        self.assertEqual(res3, False)
        self.assertEqual(res4, False)
        self.assertEqual(res5, False)
        self.assertEqual(res6, False)
        self.assertEqual(res7, False)
        self.assertEqual(res8, False)
        self.assertEqual(res9, False)
