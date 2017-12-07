# N-Queens II
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer_num = 0
        cur_nums = []
        cur_state = 0

        def search(depth):
            nonlocal cur_state, answer_num, cur_nums, n
            if depth == n:
                answer_num += 1
                return
            for num in range(n):
                tmp = (1 << num)
                if (cur_state & tmp) == 0:
                    for i_index, j_index in enumerate(cur_nums):
                        if abs(i_index - depth) == abs(j_index - num):
                            break
                    else:
                        cur_state |= tmp
                        cur_nums.append(num)
                        search(depth + 1)
                        cur_nums.pop()
                        cur_state ^= tmp
        search(0)
        return answer_num
