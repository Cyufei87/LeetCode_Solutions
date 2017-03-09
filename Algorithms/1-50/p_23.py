# Merge k Sorted Lists
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq

        class MyHeap(object):
            def __init__(self, initial=None, key=lambda x: x):
                self.key = key
                if initial:
                    self._data = [(key(item), idx, item) for idx, item in enumerate(initial)]
                    self._id = len(initial)
                    heapq.heapify(self._data)
                else:
                    self._data = []
                    self._id = 0

            def push(self, item):
                self._id += 1
                heapq.heappush(self._data, (self.key(item), self._id, item))

            def pop(self):
                return heapq.heappop(self._data)[2]

            def length(self):
                return len(self._data)

        h = MyHeap(key=lambda k: k.val)
        for l in lists:
            if l is not None:
                h.push(l)
        r = ListNode(None)
        cur = r
        while h.length() > 0:
            node = h.pop()
            cur.next = node
            cur = node
            if node.next is not None:
                h.push(node.next)
        return r.next