# -*- coding: utf8 -*-
# Integer to Roman
# 参考: baidubaike - 罗马数字
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        pre_save = [
            ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["", "M", "MM", "MMM"],
        ]
        res = ""
        res += pre_save[3][num / 1000 % 10]
        res += pre_save[2][num / 100 % 10]
        res += pre_save[1][num / 10 % 10]
        res += pre_save[0][num % 10]
        return res
