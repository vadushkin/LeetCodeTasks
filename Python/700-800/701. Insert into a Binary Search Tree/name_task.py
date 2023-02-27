"""
You are given the root node of a binary search
tree (BST) and a value to insert into the tree.
Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist
Notice that there may exist multiple valid ways for the
insertion, as long as the tree remains a BST after

* Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:


* Example 2:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

* Example 3:
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]

Constraints:

* [0, 104]
* -108 <= Node.val <= 108
* Node.val
* -108 <= val <= 108
* val
"""