import unittest

import v1
import v2
import v3


class V1PerfectNumberTestCase(unittest.TestCase):
    def test_correct_results(self):
        sol = v1.Solution()

        res1 = sol.checkPerfectNumber(6)
        res2 = sol.checkPerfectNumber(6)
        res3 = sol.checkPerfectNumber(496)
        res4 = sol.checkPerfectNumber(8128)
        res5 = sol.checkPerfectNumber(33550336)

        self.assertEqual(res1, True)
        self.assertEqual(res2, True)
        self.assertEqual(res3, True)
        self.assertEqual(res4, True)
        self.assertEqual(res5, True)

    def test_failure_results(self):
        sol = v1.Solution()

        res1 = sol.checkPerfectNumber(1513)
        res2 = sol.checkPerfectNumber(1)
        res3 = sol.checkPerfectNumber(51)
        res4 = sol.checkPerfectNumber(651436141)
        res5 = sol.checkPerfectNumber(513541)

        self.assertEqual(res1, False)
        self.assertEqual(res2, False)
        self.assertEqual(res3, False)
        self.assertEqual(res4, False)
        self.assertEqual(res5, False)


class V2PerfectNumberTestCase(unittest.TestCase):
    def test_correct_results(self):
        sol = v2.Solution()

        res1 = sol.checkPerfectNumber(6)
        res2 = sol.checkPerfectNumber(6)
        res3 = sol.checkPerfectNumber(496)
        res4 = sol.checkPerfectNumber(8128)
        res5 = sol.checkPerfectNumber(33550336)

        self.assertEqual(res1, True)
        self.assertEqual(res2, True)
        self.assertEqual(res3, True)
        self.assertEqual(res4, True)
        self.assertEqual(res5, True)

    def test_failure_results(self):
        sol = v2.Solution()

        res1 = sol.checkPerfectNumber(1513)
        res2 = sol.checkPerfectNumber(1)
        res3 = sol.checkPerfectNumber(51)
        res4 = sol.checkPerfectNumber(651436141)
        res5 = sol.checkPerfectNumber(513541)

        self.assertEqual(res1, False)
        self.assertEqual(res2, False)
        self.assertEqual(res3, False)
        self.assertEqual(res4, False)
        self.assertEqual(res5, False)


class V3PerfectNumberTestCase(unittest.TestCase):
    def test_correct_results(self):
        sol = v3.Solution()

        res1 = sol.checkPerfectNumber(6)
        res2 = sol.checkPerfectNumber(6)
        res3 = sol.checkPerfectNumber(496)
        res4 = sol.checkPerfectNumber(8128)
        res5 = sol.checkPerfectNumber(33550336)

        self.assertEqual(res1, True)
        self.assertEqual(res2, True)
        self.assertEqual(res3, True)
        self.assertEqual(res4, True)
        self.assertEqual(res5, True)

    def test_failure_results(self):
        sol = v3.Solution()

        res1 = sol.checkPerfectNumber(1513)
        res2 = sol.checkPerfectNumber(1)
        res3 = sol.checkPerfectNumber(51)
        res4 = sol.checkPerfectNumber(651436141)
        res5 = sol.checkPerfectNumber(513541)

        self.assertEqual(res1, False)
        self.assertEqual(res2, False)
        self.assertEqual(res3, False)
        self.assertEqual(res4, False)
        self.assertEqual(res5, False)
