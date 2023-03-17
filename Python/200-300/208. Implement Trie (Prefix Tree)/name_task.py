"""
A trie (pronounced as "try") or prefix tree is a
tree data structure used to efficiently store and retrieve keys
in a dataset of strings. There are various applications of

* Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:

* Trie()
* void insert(String word)
* boolean search(String word)
* boolean startsWith(String prefix)
* 1 <= word.length, prefix.length <= 2000
* word
* 3 * 104
"""