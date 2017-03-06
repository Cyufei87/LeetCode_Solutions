# String to Integer (atoi)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        n = ""
        i = 0
        str = str.strip()
        l = len(str)
        has_d = False
        if i < l and str[i] in {"-", "+"}:
            i += 1
        while i < l and str[i].isdigit():
            i += 1
        str = str[:i]
        try:
            r = int(str)
            if r < -2147483648:
                return -2147483648
            elif r >= 2147483648:
                return 2147483647
            return r
        except:
            return 0
