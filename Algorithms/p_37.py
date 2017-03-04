# -*- coding: utf8 -*-
# Sudoku Solver
# 重点是，用三个长度为9的整型数组存储当前的状态，之后不断深搜即可。
class Solution(object):
    def deep_search(self, board, state, place):
        if place > 80:
            return True
        i = place / 9
        j = place % 9
        if board[i][j] == ".":
            k = (i/3)*3 + j/3
            for digit in range(1, 10):
                flag = (1 << digit)
                if (state[0][i] & flag) == 0 and (state[1][j] & flag) == 0 and (state[2][k] & flag) == 0:
                    state[0][i] |= flag
                    state[1][j] |= flag
                    state[2][k] |= flag
                    if self.deep_search(board, state, place + 1):
                        board[i][j] = str(digit)
                        return True
                    state[0][i] ^= flag
                    state[1][j] ^= flag
                    state[2][k] ^= flag
            return False
        else:
            return self.deep_search(board, state, place + 1)

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        state = [[0]*9, [0]*9, [0]*9]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    num_flag = (1 << num)
                    state[0][i] |= num_flag
                    state[1][j] |= num_flag
                    state[2][(i/3)*3 + j/3] |= num_flag
        self.deep_search(board, state, 0)
