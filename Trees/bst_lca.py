"""
HackerRank: https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor
You are given pointer to the root of the binary search tree and two values and
you need to return the lowest common ancestor (LCA) of  and  in the binary search tree.

Example:
         4
       /   \
      2     7
     / \   /
    1   3 6

v1 = 1, v2 = 7
LCA = 4
"""
from TreeNode import TreeNode as tn

def buildBST():
    root = tn(4)

    root.left = tn(2)
    root.right = tn(7)

    root.left.left = tn(1)
    root.left.right = tn(3)
    root.right.left = tn(6)

    return root

def lca(root, v1, v2):
    if root.val > v1 and root.val > v2:
        return lca(root.left, v1, v2)
    elif root.val < v1 and root.val < v2:
        return lca(root.right, v1, v2)
    else:
        return root.val

if __name__ == '__main__':
    root = buildBST()
    print(lca(root, 1, 3))
