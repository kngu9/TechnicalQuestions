from TreeNode import TreeNode

class Solution(object):
    def dfs(self, root):
        if not root:
            return 0

        l = self.dfs(root.left)
        r = self.dfs(root.right)

        if l + r > self.maxDiameter:
            self.maxDiameter = l + r

        return max(l + 1, r + 1)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxDiameter = 0

        self.dfs(root)

        return self.maxDiameter

if __name__ == '__main__':
    """       1
             / \
            2   3
           / \
          4   5
    """
    root = TreeNode(1)

    n2 = TreeNode(2)
    n3 = TreeNode(3)

    root.left = n2
    root.right = n3

    n4 = TreeNode(4)
    n5 = TreeNode(5)

    n2.left = n4
    n3.right = n5

    s = Solution()

    diameter = s.diameterOfBinaryTree(root)

    print(diameter)
