"""
HackerRank: https://www.hackerrank.com/challenges/is-binary-search-tree

Given the root node of a binary tree, can you determine if it's also a binary search tree?

Example:

     3
   /   \
  5     2
 / \   /
1   4 6

Answer: No

     7
   /   \
  4     9
 / \   /
1   5 8

Answer: Yes
"""
from TreeNode import TreeNode as tn

def createInvalidBST():
    root = tn(3)

    root.left = tn(5)
    root.right = tn(2)

    root.left.left = tn(1)
    root.left.right = tn(4)
    root.right.left = tn(6)

    return root

def createValidBST():
    root = tn(7)

    root.left = tn(4)
    root.right = tn(9)

    root.left.left = tn(1)
    root.left.right = tn(5)
    root.right.left = tn(8)

    return root

def verifyTree(root):
    if not root:
        return True

    if root.left:
        if root.left.val > root.val:
            return False

    if root.right:
        if root.right.val < root.val:
            return False

    return verifyTree(root.left) or verifyTree(root.right)

if __name__ == '__main__':
    invalidRoot = createInvalidBST()
    validRoot = createValidBST()

    print(verifyTree(invalidRoot))
    print(verifyTree(validRoot))
