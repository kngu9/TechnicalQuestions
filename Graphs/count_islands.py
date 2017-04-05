""" Given a 2d grid map of '1's (land) and '0's (water), count the number of
    islands. An island is surrounded by water and is formed by connecting
    adjacent lands horizontally or vertically. You may assume all four edges of
    the grid are all surrounded by water. """

# Time Complexity: O(n)
# Space Complexity: O(1)
# What we are doing here is we iterate through all nxm elements, and if we see a 1
# then we recursively do a depth first search of all adjacent elements of that elements
# and mark them as searched

class Solution(object):
    def dfs(self, grid, x, y):
        if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0 or grid[x][y] != "1":
            return

        grid[x][y] = '0'

        self.dfs(grid, x+1, y)
        self.dfs(grid, x-1, y)
        self.dfs(grid, x, y+1)
        self.dfs(grid, x, y-1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0

        for i, v in enumerate(grid):
            for j, v2 in enumerate(grid[i]):
                if grid[i][j] == '1':
                    islands += 1
                    self.dfs(grid, i, j)

        return islands

m = [['1', '1', '0', '0', '0'],
     ['1', '1', '0', '0', '0'],
     ['0', '0', '1', '0', '0'],
     ['0', '0', '0', '1', '1']]

s = Solution()
print(s.numIslands(m))
