import unittest

import v1
import v2


class V1TopKFrequentWordsTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v1.Solution()

        res1 = sol.topKFrequent(["hello", "hello", "i", "i", "i"], 2)
        res2 = sol.topKFrequent(["no", "hello", "no"], 1)
        res3 = sol.topKFrequent(["welcome", "welcome"], 1)
        res4 = sol.topKFrequent(["world", "world", "world"], 1)
        res5 = sol.topKFrequent(["Yan", "Misha", "Maksim", "no", "yes", "no", "yes"], 4)

        self.assertEqual(res1, ["i", "hello"])
        self.assertEqual(res2, ["no"])
        self.assertEqual(res3, ["welcome"])
        self.assertEqual(res4, ["world"])
        self.assertEqual(res5, ["no", "yes", "Maksim", "Misha"])

    def test_failure_answers(self):
        sol = v1.Solution()

        res1 = sol.topKFrequent(["hello", "hello", "i", "i", "i"], 2)
        res2 = sol.topKFrequent(["no", "hello", "no"], 1)
        res3 = sol.topKFrequent(["welcome", "welcome"], 1)
        res4 = sol.topKFrequent(["world", "world", "world"], 1)
        res5 = sol.topKFrequent(["Yan", "Misha", "Maksim", "no", "yes", "no", "yes"], 4)

        self.assertFalse(res1 != ["i", "hello"])
        self.assertFalse(res2 != ["no"])
        self.assertFalse(res3 != ["welcome"])
        self.assertFalse(res4 != ["world"])
        self.assertFalse(res5 != ["no", "yes", "Maksim", "Misha"])


class V2TopKFrequentWordsTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v2.Solution()

        res1 = sol.topKFrequent(["hello", "hello", "i", "i", "i"], 2)
        res2 = sol.topKFrequent(["no", "hello", "no"], 1)
        res3 = sol.topKFrequent(["welcome", "welcome"], 1)
        res4 = sol.topKFrequent(["world", "world", "world"], 1)
        res5 = sol.topKFrequent(["Yan", "Misha", "Maksim", "no", "yes", "no", "yes"], 4)

        self.assertEqual(res1, ["i", "hello"])
        self.assertEqual(res2, ["no"])
        self.assertEqual(res3, ["welcome"])
        self.assertEqual(res4, ["world"])
        self.assertEqual(res5, ["no", "yes", "Maksim", "Misha"])

    def test_failure_answers(self):
        sol = v2.Solution()

        res1 = sol.topKFrequent(["hello", "hello", "i", "i", "i"], 2)
        res2 = sol.topKFrequent(["no", "hello", "no"], 1)
        res3 = sol.topKFrequent(["welcome", "welcome"], 1)
        res4 = sol.topKFrequent(["world", "world", "world"], 1)
        res5 = sol.topKFrequent(["Yan", "Misha", "Maksim", "no", "yes", "no", "yes"], 4)

        self.assertFalse(res1 != ["i", "hello"])
        self.assertFalse(res2 != ["no"])
        self.assertFalse(res3 != ["welcome"])
        self.assertFalse(res4 != ["world"])
        self.assertFalse(res5 != ["no", "yes", "Maksim", "Misha"])
