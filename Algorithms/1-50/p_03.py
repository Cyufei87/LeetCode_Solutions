# Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        t = ""
        for subs in s:
            f = t.find(subs)
            if f == -1:
                t += subs
            else:
                if len(t) > m:
                    m = len(t)
                t = t[f+1:] + subs
        if len(t) > m:
            m = len(t)
        return m