"""
Given a n * n matrix grid of 0's and
1's only. We want to represent the grid with a
Notice that you can assign the value of a node
to True or False when isLeaf is False, and both
A Quad-Tree is a tree data structure in which each
internal node has exactly four children. Besides, each node has
We can construct a Quad-Tree from a two-dimensional area using
If you want to know more about the Quad-Tree, you
The output represents the serialized format of a Quad-Tree using
level order traversal, where null signifies a path terminator where
It is very similar to the serialization of the binary
tree. The only difference is that the node is represented
If the value of isLeaf or val is True we
represent it as 1 in the list [isLeaf, val] and
if the value of isLeaf or val is False we

* Example 1:
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
* Example 2:
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.


* Example 3:
Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:


Constraints:

* val
* isLeaf
* 1's
* isLeaf
* n == grid.length == grid[i].length
* n == 2x
"""