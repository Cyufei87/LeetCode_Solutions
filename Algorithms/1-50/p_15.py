# 3Sum
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = []
        e = {}
        e2 ={}
        snums = sorted(nums)
        nums= [None, None, None]
        for n in snums:
            if n != nums[-1] or n!=nums[-2]:
                e2[n] = 1
                nums.append(n)
            elif n == 0 and n != nums[-3]:
                e2[n] = 1
                nums.append(n)
        nums = nums[3:]
        l = len(nums)
        for i, v1 in enumerate(nums):
            if i > 0 and nums[i-1] == v1:
                pass
            for j, v2 in enumerate(nums[i+1:], i+1):
                v3 = -(v1+v2)
                if v3 in e2 and (v3 >v2 or (v3==v2 and j+1<l and nums[j+1]==v2)):
                    t = sorted([v1,v2,v3])
                    h = "%s_%s_%s" % tuple(t)
                    if h not in e:
                        r.append(t)
                        e[h] = 1
        return r