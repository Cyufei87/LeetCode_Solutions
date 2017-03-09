# Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        zip_strs = zip(*strs)
        r = ""
        for tmp in zip_strs:
            if len(set(tmp)) == 1:
                r += tmp[0]
            else:
                break
        return r