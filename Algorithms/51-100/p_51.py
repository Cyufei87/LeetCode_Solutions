# N-Queens
class Solution:
    def __init__(self):
        self.answers = []
        self.cur_nums = []
        self.cur_state = 0
        self.n = 0

    def search(self, depth):
        if depth == self.n:
            cur_answer = [["." for _ in range(self.n)] for _ in range(self.n)]
            for i, num in enumerate(self.cur_nums):
                cur_answer[i][num] = "Q"
            self.answers.append(["".join(line) for line in cur_answer])
            return
        for num in range(self.n):
            tmp = (1 << num)
            if (self.cur_state & tmp) == 0:
                for i_index, j_index in enumerate(self.cur_nums):
                    if abs(i_index - depth) == abs(j_index - num):
                        break
                else:
                    self.cur_state |= tmp
                    self.cur_nums.append(num)
                    self.search(depth + 1)
                    self.cur_nums.pop()
                    self.cur_state ^= tmp

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.answers = []
        self.cur_nums = []
        self.cur_state = 0
        self.n = n
        self.search(0)
        return self.answers
