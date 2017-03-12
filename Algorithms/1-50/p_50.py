class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 1:
            return 1
        elif x == -1:
            return 1 if n % 2 == 0 else -1
        if n < 0:
            x = 1.0/x
            n = -n
        res = 1
        for _ in xrange(n):
            res *= x
            if res == 0:
                return 0
        return res
    