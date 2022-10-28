# import unittest
#
# import v1
# import v2
# import v3
#
#
# class V1GroupAnagramsTestCase(unittest.TestCase):
#     def test_correct_answers(self):
#         sol = v1.Solution()
#
#         res1 = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
#         res2 = sol.groupAnagrams([""])
#         res3 = sol.groupAnagrams(["a"])
#         res4 = sol.groupAnagrams(["cookie", "pan", "can", "nation"])
#         res5 = sol.groupAnagrams(["right", "fight", "tight", "might"])
#         res6 = sol.groupAnagrams(["own", "now", "wow", "feel", "leef"])
#
#         self.assertEqual(res1, [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
#         self.assertEqual(res2, [[""]])
#         self.assertEqual(res3, [["a"]])
#         self.assertEqual(res4, [["nation"], ["can"], ["pan"], ["cookie"]])
#         self.assertEqual(res5, [["might"], ["fight"], ["tight"], ["right"]])
#         self.assertEqual(res6, [["feel", "leef"], ["wow"], ["now", "own"]])
#
#
# class V2GroupAnagramsTestCase(unittest.TestCase):
#     def test_correct_answers(self):
#         sol = v2.Solution()
#
#         res1 = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
#         res2 = sol.groupAnagrams([""])
#         res3 = sol.groupAnagrams(["a"])
#         res4 = sol.groupAnagrams(["cookie", "pan", "can", "nation"])
#         res5 = sol.groupAnagrams(["right", "fight", "tight", "might"])
#         res6 = sol.groupAnagrams(["own", "now", "wow", "feel", "leef"])
#
#         self.assertEqual(res1, [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
#         self.assertEqual(res2, [[""]])
#         self.assertEqual(res3, [["a"]])
#         self.assertEqual(res4, [["nation"], ["can"], ["pan"], ["cookie"]])
#         self.assertEqual(res5, [["might"], ["fight"], ["tight"], ["right"]])
#         self.assertEqual(res6, [["feel", "leef"], ["wow"], ["now", "own"]])
#
#
# class V3GroupAnagramsTestCase(unittest.TestCase):
#     def test_correct_answers(self):
#         sol = v3.Solution()
#
#         res1 = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
#         res2 = sol.groupAnagrams([""])
#         res3 = sol.groupAnagrams(["a"])
#         res4 = sol.groupAnagrams(["cookie", "pan", "can", "nation"])
#         res5 = sol.groupAnagrams(["right", "fight", "tight", "might"])
#         res6 = sol.groupAnagrams(["own", "now", "wow", "feel", "leef"])
#
#         self.assertEqual(res1, [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
#         self.assertEqual(res2, [[""]])
#         self.assertEqual(res3, [["a"]])
#         self.assertEqual(res4, [["nation"], ["can"], ["pan"], ["cookie"]])
#         self.assertEqual(res5, [["might"], ["fight"], ["tight"], ["right"]])
#         self.assertEqual(res6, [["feel", "leef"], ["wow"], ["now", "own"]])
