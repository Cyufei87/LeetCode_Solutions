# Permutations II
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = len(nums)
        import copy
        res = []
        flags = [False] * l
        cur_nums = [0] * l

        def deep_search(depth):
            if depth == l:
                return res.append(copy.copy(cur_nums))
            last_num = None
            for i, num in enumerate(nums):
                if not flags[i] and num != last_num:
                    flags[i] = True
                    cur_nums[depth] = num
                    deep_search(depth + 1)
                    flags[i] = False
                    last_num = num

        deep_search(0)
        return res
