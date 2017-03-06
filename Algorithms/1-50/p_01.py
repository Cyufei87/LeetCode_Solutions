# Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = None
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] +nums[j] == target:
                    r = [i, j]
                    break
            if r:
                break
        return r