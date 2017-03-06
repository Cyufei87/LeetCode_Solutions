# Add Two Numbers
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        d1 = l1.val
        cal = 1
        while l1.next is not None:
            l1 = l1.next
            cal *= 10
            d1 += l1.val*cal
        d2 = l2.val
        cal = 1
        while l2.next is not None:
            l2 = l2.next
            cal *= 10
            d2 += l2.val*cal
        d = d1+d2
        l = ListNode(d%10)
        d = d/10
        r = l
        while d>0:
            l.next = ListNode(d%10)
            d = d/10
            l = l.next
        return r