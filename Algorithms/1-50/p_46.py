# Permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        import copy
        res = []
        flags = [False] * l
        cur_nums = [0] * l
        
        def deep_search(depth):
            if depth == l:
                return res.append(copy.copy(cur_nums))
            for i, num in enumerate(nums):
                if not flags[i]:
                    flags[i] = True
                    cur_nums[depth] = nums[i]
                    deep_search(depth + 1)
                    flags[i] = False
        
        deep_search(0)
        return res
