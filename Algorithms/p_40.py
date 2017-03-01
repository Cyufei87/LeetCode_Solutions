# Combination Sum II
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        can_len = len(candidates)
        result = []
        cur_list = []
        import copy
        def deep_search(cur_list_len, num, index):
            last_num = None
            while index < can_len:
                if candidates[index] != last_num:
                    last_num = candidates[index]
                    if num + candidates[index] < target:
                        cur_list.append(candidates[index])
                        deep_search(cur_list_len+1, num+candidates[index], index+1)
                        del cur_list[cur_list_len]
                    elif num + candidates[index] == target:
                        valid_list = copy.copy(cur_list)
                        valid_list.append(candidates[index])
                        result.append(valid_list)
                    else:
                        break
                index += 1
        deep_search(0, 0, 0)
        return result