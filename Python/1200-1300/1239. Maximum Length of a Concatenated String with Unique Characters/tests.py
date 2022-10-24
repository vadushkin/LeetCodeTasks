import unittest

import v1
import v2


class V1MaxiLenOfConcatenatedStrWithUniqCharsTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v1.Solution()

        res1 = sol.maxLength(["asd", "ds", "qw", "cx"])
        res2 = sol.maxLength(["g", "dsd", "q", "cqx"])
        res3 = sol.maxLength(["zxc", "asd", "qwe", "cvb"])
        res4 = sol.maxLength(["f", "b", "vv", "aa"])
        res5 = sol.maxLength(["ferwe", "bqwer", "vrewqwev", "aare"])
        res6 = sol.maxLength(["zxcvbnm", "asdfghjk", "qwertyui"])

        self.assertEqual(res1, 7)
        self.assertEqual(res2, 4)
        self.assertEqual(res3, 9)
        self.assertEqual(res4, 2)
        self.assertEqual(res5, 5)
        self.assertEqual(res6, 23)


class V2MaxiLenOfConcatenatedStrWithUniqCharsTestCase(unittest.TestCase):
    def test_correct_answers(self):
        sol = v2.Solution()

        res1 = sol.maxLength(["asd", "ds", "qw", "cx"])
        res2 = sol.maxLength(["g", "dsd", "q", "cqx"])
        res3 = sol.maxLength(["zxc", "asd", "qwe", "cvb"])
        res4 = sol.maxLength(["f", "b", "vv", "aa"])
        res5 = sol.maxLength(["ferwe", "bqwer", "vrewqwev", "aare"])
        res6 = sol.maxLength(["zxcvbnm", "asdfghjk", "qwertyui"])

        self.assertEqual(res1, 7)
        self.assertEqual(res2, 4)
        self.assertEqual(res3, 9)
        self.assertEqual(res4, 2)
        self.assertEqual(res5, 5)
        self.assertEqual(res6, 23)
