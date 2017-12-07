# Spiral Matrix
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        results = []
        row_num = len(matrix)
        column_num = len(matrix[0])
        access_matrix = [[False] * column_num for _ in range(row_num)]
        element_num = row_num * column_num
        cur_i, cur_j = 0, -1
        cur_dir = "right"
        while len(results) < element_num:
            # print(cur_i, cur_j)
            if cur_dir == "right":
                if cur_j + 1 < column_num and not access_matrix[cur_i][cur_j + 1]:
                    cur_j += 1
                else:
                    cur_dir = "down"
                    continue
            elif cur_dir == "down":
                if cur_i + 1 < row_num and not access_matrix[cur_i + 1][cur_j]:
                    cur_i += 1
                else:
                    cur_dir = "left"
                    continue
            elif cur_dir == "left":
                if cur_j - 1 >= 0 and not access_matrix[cur_i][cur_j - 1]:
                    cur_j -= 1
                else:
                    cur_dir = "up"
                    continue
            elif cur_dir == "up":
                if cur_i - 1 >= 0 and not access_matrix[cur_i - 1][cur_j]:
                    cur_i -= 1
                else:
                    cur_dir = "right"
                    continue
            access_matrix[cur_i][cur_j] = True
            results.append(matrix[cur_i][cur_j])
        return results
