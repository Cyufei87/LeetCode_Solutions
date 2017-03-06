# Reverse Integer
class Solution(object):
    def reverse_str(self, x):
        l = list(x)
        l.reverse()
        return "".join(l)

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            a = -1 * int(self.reverse_str(str(-x)))
            if a < -2147483648:
                return 0
            else:
                return a
        else:
            a = int(self.reverse_str(str(x)))
            if a >= 2147483648:
                return 0
            return a

