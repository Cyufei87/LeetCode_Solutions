# Spiral Matrix II
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return []

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        x = 0
        y = 0
        dir_ = 'right'
        cur_v = 1
        matrix[0][0] = cur_v
        while cur_v < n * n:
            if dir_ == 'right':
                if y + 1 < n and matrix[x][y + 1] == 0:
                    y += 1
                else:
                    dir_ = 'down'
                    continue
            elif dir_ == 'down':
                if x + 1 < n and matrix[x + 1][y] == 0:
                    x += 1
                else:
                    dir_ = 'left'
                    continue
            elif dir_ == 'left':
                if y > 0 and matrix[x][y - 1] == 0:
                    y -= 1
                else:
                    dir_ = 'up'
                    continue
            elif dir_ == 'up':
                if x > 0 and matrix[x - 1][y] == 0:
                    x -= 1
                else:
                    dir_ = 'right'
                    continue
            cur_v += 1
            matrix[x][y] = cur_v
        return matrix
