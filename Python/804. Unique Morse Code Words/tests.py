import unittest

import v1
import v2


class V1UniqueMorseCodeWordsTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v1.Solution()

        res1 = sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
        res2 = sol.uniqueMorseRepresentations(["dweller", "zen", ])
        res3 = sol.uniqueMorseRepresentations(["dweller", "gig", "monster"])
        res4 = sol.uniqueMorseRepresentations(["dweller", "zen", "monster"])
        res5 = sol.uniqueMorseRepresentations(["dweller", "zen", "cool", "monster"])
        res6 = sol.uniqueMorseRepresentations(["gin", "zen", "cool", "impressive"])
        res7 = sol.uniqueMorseRepresentations(["king", "nice", "impressive"])
        res8 = sol.uniqueMorseRepresentations(["king", "nice", "gig", "impressive"])
        res9 = sol.uniqueMorseRepresentations(["gin", "nice", "gig", "msg"])
        res10 = sol.uniqueMorseRepresentations(["king", "zen"])

        self.assertEqual(res1, 2)
        self.assertEqual(res2, 2)
        self.assertEqual(res3, 3)
        self.assertEqual(res4, 3)
        self.assertEqual(res5, 4)
        self.assertEqual(res6, 3)
        self.assertEqual(res7, 3)
        self.assertEqual(res8, 4)
        self.assertEqual(res9, 3)
        self.assertEqual(res10, 2)

    def test_failure_answers(self):
        sol = v1.Solution()

        res1 = sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
        res2 = sol.uniqueMorseRepresentations(["dweller", "zen", ])
        res3 = sol.uniqueMorseRepresentations(["dweller", "gig", "monster"])
        res4 = sol.uniqueMorseRepresentations(["dweller", "zen", "monster"])
        res5 = sol.uniqueMorseRepresentations(["dweller", "zen", "cool", "monster"])
        res6 = sol.uniqueMorseRepresentations(["gin", "zen", "cool", "impressive"])
        res7 = sol.uniqueMorseRepresentations(["king", "nice", "impressive"])
        res8 = sol.uniqueMorseRepresentations(["king", "nice", "gig", "impressive"])
        res9 = sol.uniqueMorseRepresentations(["gin", "nice", "gig", "msg"])
        res10 = sol.uniqueMorseRepresentations(["king", "zen"])

        self.assertFalse(res1 != 2)
        self.assertFalse(res2 != 2)
        self.assertFalse(res3 != 3)
        self.assertFalse(res4 != 3)
        self.assertFalse(res5 != 4)
        self.assertFalse(res6 != 3)
        self.assertFalse(res7 != 3)
        self.assertFalse(res8 != 4)
        self.assertFalse(res9 != 3)
        self.assertFalse(res10 != 2)


class V2UniqueMorseCodeWordsTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v2.Solution()

        res1 = sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
        res2 = sol.uniqueMorseRepresentations(["dweller", "zen", ])
        res3 = sol.uniqueMorseRepresentations(["dweller", "gig", "monster"])
        res4 = sol.uniqueMorseRepresentations(["dweller", "zen", "monster"])
        res5 = sol.uniqueMorseRepresentations(["dweller", "zen", "cool", "monster"])
        res6 = sol.uniqueMorseRepresentations(["gin", "zen", "cool", "impressive"])
        res7 = sol.uniqueMorseRepresentations(["king", "nice", "impressive"])
        res8 = sol.uniqueMorseRepresentations(["king", "nice", "gig", "impressive"])
        res9 = sol.uniqueMorseRepresentations(["gin", "nice", "gig", "msg"])
        res10 = sol.uniqueMorseRepresentations(["king", "zen"])

        self.assertEqual(res1, 2)
        self.assertEqual(res2, 2)
        self.assertEqual(res3, 3)
        self.assertEqual(res4, 3)
        self.assertEqual(res5, 4)
        self.assertEqual(res6, 3)
        self.assertEqual(res7, 3)
        self.assertEqual(res8, 4)
        self.assertEqual(res9, 3)
        self.assertEqual(res10, 2)

    def test_failure_answers(self):
        sol = v2.Solution()

        res1 = sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
        res2 = sol.uniqueMorseRepresentations(["dweller", "zen", ])
        res3 = sol.uniqueMorseRepresentations(["dweller", "gig", "monster"])
        res4 = sol.uniqueMorseRepresentations(["dweller", "zen", "monster"])
        res5 = sol.uniqueMorseRepresentations(["dweller", "zen", "cool", "monster"])
        res6 = sol.uniqueMorseRepresentations(["gin", "zen", "cool", "impressive"])
        res7 = sol.uniqueMorseRepresentations(["king", "nice", "impressive"])
        res8 = sol.uniqueMorseRepresentations(["king", "nice", "gig", "impressive"])
        res9 = sol.uniqueMorseRepresentations(["gin", "nice", "gig", "msg"])
        res10 = sol.uniqueMorseRepresentations(["king", "zen"])

        self.assertFalse(res1 != 2)
        self.assertFalse(res2 != 2)
        self.assertFalse(res3 != 3)
        self.assertFalse(res4 != 3)
        self.assertFalse(res5 != 4)
        self.assertFalse(res6 != 3)
        self.assertFalse(res7 != 3)
        self.assertFalse(res8 != 4)
        self.assertFalse(res9 != 3)
        self.assertFalse(res10 != 2)
