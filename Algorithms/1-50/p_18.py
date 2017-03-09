# 4Sum
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        snums = sorted(nums)
        num_dict = {}
        for i, v1 in enumerate(snums):
            for j, v2 in enumerate(snums[i+1:], i+1):
                num = v1+ v2
                if num not in num_dict:
                    num_dict[num] = []
                num_dict[num].append([i, j])
        r = []
        e_dict = {}
        for i, v1 in enumerate(snums):
            for j, v2 in enumerate(snums[i+1:], i+1):
                will = target - v1 -v2
                if will in num_dict:
                    for m, n in num_dict[will]:
                        if m > j:
                            tmp = [snums[i], snums[j], snums[m], snums[n]]
                            key = "%s_%s_%s_%s" % tuple(tmp)
                            if key not in e_dict:
                                r.append(tmp)
                                e_dict[key] = 1
        return r