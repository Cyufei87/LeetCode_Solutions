# Count and Say
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cur = "1"
        n -= 1
        while n > 0:
            next = ""
            cur_digit = cur[0]
            cur_num = 1
            l = 1
            while l < len(cur):
                if cur[l] == cur_digit:
                    cur_num += 1
                else:
                    next += str(cur_num)
                    next += cur_digit
                    cur_digit = cur[l]
                    cur_num = 1
                l += 1
            next += str(cur_num)
            next += cur_digit
            cur = next
            n -= 1
        return cur