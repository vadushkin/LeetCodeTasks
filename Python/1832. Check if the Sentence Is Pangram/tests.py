import unittest

import v1
import v2


class V1CheckIsPangramTestCase(unittest.TestCase):
    def test_correct_results(self):
        sol = v1.Solution()

        res1 = sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
        res2 = sol.checkIfPangram("Thequickbrownfoxjumpsoverthelazydog")
        res3 = sol.checkIfPangram("qwertyuiasdfghjkzxcvbnmolp")
        res4 = sol.checkIfPangram("QWERTYUIASDFGHJKZXCVBNMOLP")
        res5 = sol.checkIfPangram("QWERTYUIASdFGHJKZXCVBNMOLP")

        self.assertEqual(res1, True)
        self.assertEqual(res2, True)
        self.assertEqual(res3, True)
        self.assertEqual(res4, True)
        self.assertEqual(res5, True)

    def test_failure_results(self):
        sol = v1.Solution()

        res1 = sol.checkIfPangram("Hello")
        res2 = sol.checkIfPangram("Thuickbrownfoumpsovertheladog")
        res3 = sol.checkIfPangram("leetcode")
        res4 = sol.checkIfPangram("QWERTYUIASDFGHJKZXCVBNMOLl")
        res5 = sol.checkIfPangram("qwertyuiasdfghjkzxcvbnmolq")

        self.assertEqual(res1, False)
        self.assertEqual(res2, False)
        self.assertEqual(res3, False)
        self.assertEqual(res4, False)
        self.assertEqual(res5, False)


class V2CheckIsPangramTestCase(unittest.TestCase):
    def test_correct_results(self):
        sol = v2.Solution()

        res1 = sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
        res2 = sol.checkIfPangram("Thequickbrownfoxjumpsoverthelazydog")
        res3 = sol.checkIfPangram("qwertyuiasdfghjkzxcvbnmolp")
        res4 = sol.checkIfPangram("QWERTYUIASDFGHJKZXCVBNMOLP")
        res5 = sol.checkIfPangram("QWERTYUIASdFGHJKZXCVBNMOLP")

        self.assertEqual(res1, True)
        self.assertEqual(res2, True)
        self.assertEqual(res3, True)
        self.assertEqual(res4, True)
        self.assertEqual(res5, True)

    def test_failure_results(self):
        sol = v2.Solution()

        res1 = sol.checkIfPangram("Hello")
        res2 = sol.checkIfPangram("Thuickbrownfoumpsovertheladog")
        res3 = sol.checkIfPangram("leetcode")
        res4 = sol.checkIfPangram("QWERTYUIASDFGHJKZXCVBNMOLl")
        res5 = sol.checkIfPangram("qwertyuiasdfghjkzxcvbnmolq")

        self.assertEqual(res1, False)
        self.assertEqual(res2, False)
        self.assertEqual(res3, False)
        self.assertEqual(res4, False)
        self.assertEqual(res5, False)
