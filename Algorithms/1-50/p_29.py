# Divide Two Integers
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        max = (1<<31) - 1
        if divisor == 0:
            return max
        if abs(dividend) < abs(divisor):
            return 0
        v = dividend/divisor
        if v < 0 and abs(dividend)%abs(divisor) > 0:
            v += 1
        if v > max:
            return max
        return v