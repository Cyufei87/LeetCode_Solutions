# Rotate Image
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # i, j  j, n-1-i
        # i, j  n-1-j, i
        n = len(matrix)
        new_matrix = [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = new_matrix[i][j]