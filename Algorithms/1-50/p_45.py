# Jump Game II
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l <= 1:
            return 0
        min_jumps = [0] * l
        to_place = 0
        for i, num in enumerate(nums):
            if i + num >= l - 1:
                return min_jumps[i] + 1
            while i + num > to_place:
                to_place += 1
                min_jumps[to_place] = min_jumps[i] + 1