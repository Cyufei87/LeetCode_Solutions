# 3Sum Closest
class Solution(object):
    def er_fen(self, nums, i, j, num):
        if i >= j:
            return i
        if i + 1 == j:
            if nums[j] <= num:
                return j
            else:
                return i
        mid = (i+j)/2
        if nums[mid] <= num:
            return self.er_fen(nums, mid, j, num)
        else:
            return self.er_fen(nums, i, mid-1, num)

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        snums = sorted(nums)
        num_len = len(snums)
        cur_closed = snums[0] + snums[1] + snums[2]
        for i, v1 in enumerate(snums[:-2]):
            for j, v2 in enumerate(snums[i+1:-1], i+1):
                will = target - v1 - v2
                closed_idx = self.er_fen(snums, j+1, num_len-1, will)
                closed = snums[closed_idx] + v1 + v2
                if abs(target-closed) < abs(target-cur_closed):
                    cur_closed = closed
                if closed_idx < num_len - 1:
                    closed = snums[closed_idx+1] + v1 + v2
                    if abs(target-closed) < abs(target-cur_closed):
                        cur_closed = closed
                if cur_closed == target:
                    return target
        return cur_closed