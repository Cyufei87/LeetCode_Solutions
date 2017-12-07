# Maximum Subarray
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_sum = 0
        max_sum = nums[0]
        for num in nums:
            cur_sum = num if last_sum <= 0 else (last_sum + num)
            if cur_sum > max_sum:
                max_sum = cur_sum
            last_sum = cur_sum
        return max_sum
