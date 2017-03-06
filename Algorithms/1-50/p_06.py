# ZigZag Conversion
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        n = len(s)
        r = ""
        for i in range(numRows):
            tmp = i
            while tmp < n:
                r += s[tmp]
                if i > 0 and i < numRows - 1:
                    m = tmp + 2 * numRows - 2 - 2 - 2 * (i - 1)
                    if m < n:
                        r += s[m]
                tmp += 2 * numRows - 2
        return r