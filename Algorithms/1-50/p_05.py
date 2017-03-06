# Longest Palindromic Substring
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_num = 0
        max_str = ""
        slen = len(s)
        for idx, ss in enumerate(s):
            if idx < slen - 1 and s[idx+1] == ss:
                i = idx - 1
                j = idx + 2
                while i>=0 and j<slen and s[i]==s[j]:
                    i -= 1
                    j += 1
                i += 1
                j -= 1
                if j-i+1>max_num:
                    max_num = j-i+1
                    max_str = s[i:j+1]
            i = idx - 1
            j = idx + 1
            while i>=0 and j<slen and s[i]==s[j]:
                i -= 1
                j += 1
            i += 1
            j -= 1
            if j-i+1>max_num:
                max_num = j-i+1
                max_str = s[i:j+1]
        return max_str