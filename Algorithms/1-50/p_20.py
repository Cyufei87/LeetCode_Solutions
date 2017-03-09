# Valid Parentheses
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import deque
        q = deque()
        for ss in s:
            if len(q) >= 1:
                if (ss == ")" and q[-1] == "(") or (ss == "]" and q[-1] == "[") or (ss == "}" and q[-1] == "{"):
                    q.pop()
                else:
                    q.append(ss)
            else:
                q.append(ss)
        if len(q) == 0:
            return True
        return False