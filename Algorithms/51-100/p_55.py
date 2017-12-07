# Jump Game
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur_jump = 0
        nums_len = len(nums)
        for index, num in enumerate(nums):
            cur_jump = max(cur_jump - 1, num)
            if cur_jump == 0 and index < nums_len - 1:
                return False
        return True
