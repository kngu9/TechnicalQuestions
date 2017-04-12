"""
HackerRank: https://www.hackerrank.com/challenges/tree-top-view
You are given a pointer to the root of a binary tree. Print the top view of the binary tree.

Example:

     3
   /   \
  5     2
 / \   / \
1   4 6   7
 \       /
  9     8
Top View : 1 -> 5 -> 3 -> 2 -> 7

"""

from TreeNode import TreeNode as tn

def createTree():
    root = tn(3)
    root.left = tn(5)
    root.right = tn(2)

    root.left.left = tn(1)
    root.left.right = tn(4)
    root.left.left.right = tn(9)

    root.right.left = tn(6)
    root.right.right = tn(7)
    root.right.right.left = tn(8)

    return root

def verticalView(root, mp, horiz = 0):
    if not root:
        return

    if horiz not in mp:
        mp[horiz] = []

    mp[horiz].append(root.val)

    verticalView(root.left, mp, horiz-1)
    verticalView(root.right, mp, horiz+1)

def topView(root):
    ans = []
    mp = {}

    verticalView(root, mp, 0)

    for index, value in enumerate(sorted(mp)):
        ans.append(mp[value][0])

    return ans

if __name__ == '__main__':
    node = createTree()

    print(topView(node))
