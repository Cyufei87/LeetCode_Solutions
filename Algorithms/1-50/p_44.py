# Wildcard Matching
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len = len(s)
        p_len = len(p)
        dp = [[False for _ in range(p_len + 1)] for _ in range(s_len + 1)]
        dp[0][0] = True
        i = 0
        while i < p_len and p[i] == "*":
            dp[0][i + 1] = True
            i += 1
        for i, c in enumerate(s, 1):
            for j, pc in enumerate(p, 1):
                if pc == "*":
                    dp[i][j] = dp[i - 1][j] | dp[i][j - 1]
                elif pc == "?" or pc == c:
                    dp[i][j] = dp[i-1][j-1]
        return dp[s_len][p_len]