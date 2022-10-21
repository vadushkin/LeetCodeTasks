import unittest

import v1
import v2


class V1JewelsStonesTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v1.Solution()

        res1 = sol.numJewelsInStones("Aa", "AAAAa")
        res2 = sol.numJewelsInStones("QWE", "QWERTYQWERTY")
        res3 = sol.numJewelsInStones("w", "wwwwwwwww")
        res4 = sol.numJewelsInStones("q", "AAAAaq")
        res5 = sol.numJewelsInStones("ahahah", "hahaha")
        res6 = sol.numJewelsInStones("q", "q")
        res7 = sol.numJewelsInStones("okay", "yako")

        self.assertEqual(res1, 5)
        self.assertEqual(res2, 6)
        self.assertEqual(res3, 9)
        self.assertEqual(res4, 1)
        self.assertEqual(res5, 18)
        self.assertEqual(res6, 1)
        self.assertEqual(res7, 4)

    def test_empty_answers(self):
        sol = v1.Solution()

        res1 = sol.numJewelsInStones("Aa", "sd")
        res2 = sol.numJewelsInStones("im", "her")
        res3 = sol.numJewelsInStones("nevertheless", "qw")
        res4 = sol.numJewelsInStones("t", "sare")
        res5 = sol.numJewelsInStones("QQQW", "qqqw")
        res6 = sol.numJewelsInStones("qqqw", "QQQW")
        res7 = sol.numJewelsInStones("fs", "da")

        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)
        self.assertEqual(res3, 0)
        self.assertEqual(res4, 0)
        self.assertEqual(res5, 0)
        self.assertEqual(res6, 0)
        self.assertEqual(res7, 0)


class V2JewelsStonesTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v2.Solution()

        res1 = sol.numJewelsInStones("Aa", "AAAAa")
        res2 = sol.numJewelsInStones("QWE", "QWERTYQWERTY")
        res3 = sol.numJewelsInStones("w", "wwwwwwwww")
        res4 = sol.numJewelsInStones("q", "AAAAaq")
        res5 = sol.numJewelsInStones("ahahah", "hahaha")
        res6 = sol.numJewelsInStones("q", "q")
        res7 = sol.numJewelsInStones("okay", "yako")

        self.assertEqual(res1, 5)
        self.assertEqual(res2, 6)
        self.assertEqual(res3, 9)
        self.assertEqual(res4, 1)
        self.assertEqual(res5, 18)
        self.assertEqual(res6, 1)
        self.assertEqual(res7, 4)

    def test_empty_answers(self):
        sol = v2.Solution()

        res1 = sol.numJewelsInStones("Aa", "sd")
        res2 = sol.numJewelsInStones("im", "her")
        res3 = sol.numJewelsInStones("nevertheless", "qw")
        res4 = sol.numJewelsInStones("t", "sare")
        res5 = sol.numJewelsInStones("QQQW", "qqqw")
        res6 = sol.numJewelsInStones("qqqw", "QQQW")
        res7 = sol.numJewelsInStones("fs", "da")

        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)
        self.assertEqual(res3, 0)
        self.assertEqual(res4, 0)
        self.assertEqual(res5, 0)
        self.assertEqual(res6, 0)
        self.assertEqual(res7, 0)
