# Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = None
        r = 0
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if num != last:
                last = num
            else:
                nums.pop(i)
        return len(nums)