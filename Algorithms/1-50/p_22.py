# Generate Parentheses
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r = []

        def search(cur_s, num):
            if len(cur_s) == 2*n:
                r.append(cur_s)
                return
            if num < n:
                search(cur_s+"(", num+1)
            if len(cur_s) - num < num:
                search(cur_s+")", num)

        search("", 0)
        return r