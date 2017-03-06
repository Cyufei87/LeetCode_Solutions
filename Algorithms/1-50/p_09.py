# Palindrome Number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
            x = -x
        s = str(x)
        l = len(s)
        half = l/2
        ok = True
        for i in range(half+1):
            if s[i] != s[l-i-1]:
                ok = False
        return ok