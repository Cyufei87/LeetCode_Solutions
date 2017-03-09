# Regular Expression Matching
# reference: https://discuss.leetcode.com/topic/57663/python-dp-solution/4
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == "":
            a = [True, True] + [False] * len(p)
            for i in range(2, len(p)+2):
                if p[i-2] == "*":
                    a[i] = a[i-1] or a[i-2]
            return a[len(p)+1]
        s_len = len(s)
        p_len = len(p)
        dp = [[False for j in range(p_len + 1)] for i in range(s_len + 1)]
        s = " "+s
        p = " "+p
        dp[0][0] = True
        for j in range(1, p_len+1):
            if p[j] == "*":
                dp[0][j] = dp[0][j-1]
                if j > 1:
                    dp[0][j] = dp[0][j] or dp[0][j-2]
        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if s[i] == p[j] or p[j] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*":
                    if j > 1:
                        dp[i][j] = dp[i][j-2]
                    if p[j-1] == s[i] or p[j-1] == ".":
                        dp[i][j] = dp[i-1][j] or dp[i][j]
        return dp[i][j]