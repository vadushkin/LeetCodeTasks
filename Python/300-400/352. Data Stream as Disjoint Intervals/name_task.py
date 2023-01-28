"""Given a data stream input of non-negative integers a1, a2, ..., an,
summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

SummaryRanges() Initializes the object with an empty stream.
void addNum(int value) Adds the integer value to the stream.
int[][] getIntervals() Returns a summary of the integers in the stream
currently as a list of disjoint intervals [starti, endi].
The answer should be sorted by starti.

Constraints:

0 <= value <= 104
At most 3 * 104 calls will be made to addNum and getIntervals.
"""