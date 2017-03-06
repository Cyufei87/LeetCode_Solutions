# Next Permutation
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        last = nums[-1]
        t = 0
        for i in range(l-2, -1, -1):
            if nums[i] < last:
                t = i + 1
                break
            else:
                last = nums[i]
        if t > 0:
            m = nums[t-1]
            for i in range(t, l):
                if nums[i] <= m:
                    nums[t-1] = nums[i-1]
                    nums[i-1] = m
                    break
            else:
                nums[t-1] = nums[l-1]
                nums[l-1] = m
        mid = (t + l-1)/2
        for i in range(t, mid+1):
            nums[i], nums[t+l-1-i] = nums[t+l-1-i], nums[i]