# -*- coding: utf8 -*-
# Longest Valid Parentheses
# O(n)时间解决，“翻转”很重要，为了解决类似“((((((((((”的情况，“翻转”应该最多出现一次（待证明）
class Solution(object):
    def max_legal_num(self, s, letter="("):
        num = 0
        tmp = 0
        for index, i in enumerate(s):
            if i == letter:
                tmp += 1
            else:
                tmp -= 1
            if tmp == 0:
                num = index + 1
            elif tmp < 0:
                break
        return num

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_num = 0
        l = len(s)
        i = 0
        letter = "("
        while i < l:
            if s[i] == letter:
                tmp = self.max_legal_num(s[i:], letter)
                if tmp > max_num:
                    max_num = tmp
                if tmp > 0:
                    i += tmp
                else:  # 翻转
                    s = s[i+1:][::-1]
                    l = len(s)
                    i = 0
                    letter = ")" if letter == "(" else "("
            else:
                i += 1
        return max_num