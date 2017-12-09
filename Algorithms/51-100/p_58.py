# Length of Last Word
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len((s.split() or [''])[-1])
