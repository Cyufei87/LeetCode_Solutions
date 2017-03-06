# -*- coding: utf8 -*-
# Trapping Rain Water
# max_h_index存储某个点之后的最大高度的下标
# 从0开始一遍循环，根据max_h_index，可以直接计算出某个位置的积水情况
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        if l == 0:
            return 0
        max_h_index = [0] * l
        max_h_index[l-1] = l - 1
        i = l - 2
        while i >= 0:
            max_h_index[i] = i if height[i] > height[max_h_index[i+1]] else max_h_index[i+1]
            i -= 1
        i = 0
        water = 0
        while i < l-1:
            if height[i] == 0:
                i += 1
            else:
                tmp = max_h_index[i+1]
                tmp_h = height[tmp]
                if tmp_h == 0:
                    break
                else:
                    if tmp == i+1:
                        i += 1
                    else:
                        if tmp_h <= height[i]:
                            while i < tmp:
                                water += max(tmp_h - height[i], 0)
                                i += 1
                        else:
                            tmp_h = height[i]
                            while height[i] <= tmp_h:
                                water += max(tmp_h - height[i], 0)
                                i += 1
        return water