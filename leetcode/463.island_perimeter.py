class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])

        cells = 0
        for i in xrange(height):
            for j in xrange(width):
                if grid[i][j] and not (i!=height-1 and j!= width-1 and grid[i][j+1] and grid[i+1][j] and grid[i+1][j+1]):
                    cells += 1
                 
        if cells == 0:
            return 0
        return cells*2+2
