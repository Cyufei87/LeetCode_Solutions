# First Missing Positive
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        for i in range(l):
            num = nums[i]
            while 0 < num <= l:
                if nums[num-1] != num:
                    nums[num-1], nums[i] = num, nums[num-1]
                    num = nums[i]
                else:
                    break
        for i in range(l):
            if nums[i] != i+1:
                return i+1
        else:
            return l+1