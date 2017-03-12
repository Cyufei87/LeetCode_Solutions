# Group Anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        r = {}
        for s in strs:
            t = "".join(sorted(s))
            if t in r:
                r[t].append(s)
            else:
                r[t] = [s]
        return r.values()
