# Merge Intervals
class Interval:
    # Definition for an interval.
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda interval: interval.start)
        merge_intervals = []
        cur_start = intervals[0].start
        cur_end = intervals[0].end
        for interval in intervals:
            if interval.start > cur_end:
                merge_intervals.append(Interval(s=cur_start, e=cur_end))
                cur_start = interval.start
                cur_end = interval.end
            elif interval.end > cur_end:
                cur_end = interval.end
        merge_intervals.append(Interval(s=cur_start, e=cur_end))
        return merge_intervals
