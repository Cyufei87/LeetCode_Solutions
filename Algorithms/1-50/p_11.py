# Container With Most Water
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h_len = len(height)
        # s = [0] * h_len
        e = [h_len - 1] * h_len
        cur_max = 0
        s_num = 1
        e_num = 1
        '''for i, h in enumerate(height[1:], 1):
            if h > height[cur_max]:
                cur_max = i
                s_num += 1
            s[i] = cur_max'''
        cur_max = h_len - 1
        for i in range(h_len - 2, -1, -1):
            h = height[i]
            if h > height[cur_max]:
                cur_max = i
                # e_num += 1
            e[i] = cur_max
        max_con = 0
        max_h = -1
        for i, ai in enumerate(height[:-1]):
            if ai > max_h:
                max_h = ai
                cur_j = e[i + 1]
                while True:
                    aj = height[cur_j]
                    cur_con = min(ai, aj) * (cur_j - i)
                    if cur_con > max_con:
                        max_con = cur_con
                    if cur_j == h_len - 1:
                        break
                    cur_j = e[cur_j + 1]
        return max_con
