"""You are given an array of non-overlapping intervals intervals where
intervals[i] = [starti, endi] represent the start and the end of the ith
interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that
represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still
sorted in ascending order by starti and intervals still does not
have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""