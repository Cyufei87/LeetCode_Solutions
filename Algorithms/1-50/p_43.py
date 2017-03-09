# Multiply Strings
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        reversed_num1 = num1[::-1]
        reversed_num2 = num2[::-1]
        for i, digit1 in enumerate(reversed_num2):
            for j, digit2 in enumerate(reversed_num1):
                d1 = int(digit1)
                d2 = int(digit2)
                res[i + j] += d1 * d2
        l = len(res)
        i = 0
        while i < l - 1:
            res[i+1] += res[i] / 10
            res[i] %= 10
            i += 1
        ans = ("".join(map(str, res)))[::-1].lstrip("0")
        return ans if ans else "0"
