"""
HackerRank: https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor
You are given pointer to the root of the binary tree and two values and
you need to return the lowest common ancestor (LCA) of  and  in the binary tree.

Example:
         3
       /   \
      6     8
     / \     \
    2  11    13
      /  \  /
     9   5  7

v1 = 2, v2 = 8
LCA = 3
"""

from TreeNode import TreeNode as tn

def buildTree():
    root = tn(3)

    root.left = tn(6)
    root.right = tn(8)

    root.left.left = tn(2)
    root.left.right = tn(11)
    root.right.right = tn(13)

    root.left.right.left = tn(9)
    root.left.right.right = tn(5)
    root.right.right.left = tn(7)

    return root

def lcaBT(root, v1, v2):
    if not root:
        return None

    if root.val == v1 or root.val == v2:
        return root

    left = lcaBT(root.left, v1, v2)
    right = lcaBT(root.right, v1, v2)

    if not root.left and not root.right:
        return None

    if root.left and root.right:
        return root

    return left if left else right

if __name__ == '__main__':
    root = buildTree()

    print(lcaBT(root, 2, 11).val)
