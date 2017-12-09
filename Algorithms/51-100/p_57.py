# Insert Interval


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        merge_interval = Interval(s=newInterval.start, e=newInterval.end)
        for index, interval in enumerate(intervals):
            if interval.end < newInterval.start:
                result.append(interval)
            elif interval.start > newInterval.end:
                result.append(merge_interval)
                result.extend(intervals[index:])
                break
            else:
                if interval.start < merge_interval.start:
                    merge_interval.start = interval.start
                if interval.end > merge_interval.end:
                    merge_interval.end = interval.end
        else:
            result.append(merge_interval)
        return result
