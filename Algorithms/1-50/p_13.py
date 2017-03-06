# Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        chr_dict = {
            "I": 1,
            "X": 10,
            "C": 100,
            "M": 1000,
            "V": 5,
            "L": 50,
            "D": 500,
        }
        sum_value = 0
        i = 1
        last_num = chr_dict[s[0]]
        cur_value = last_num
        while i < len(s):
            num = chr_dict[s[i]]
            if num > last_num:
                cur_value = num - cur_value
                last_num = num
            elif num == last_num:
                cur_value += num
            else:
                if last_num / 5 == num:
                    cur_value += num
                    last_num = num
                else:
                    sum_value += cur_value
                    cur_value = num
                    last_num = num
            i += 1
        sum_value += cur_value
        return sum_value
