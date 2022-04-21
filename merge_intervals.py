#Question -> https://leetcode.com/problems/merge-intervals/
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        merge_intervals = []
        
        for interval in sorted(intervals):
            if len(merge_intervals) == 0 or merge_intervals[-1][-1] < interval[0]:
                merge_intervals.append(interval)
            else:
                merge_intervals[-1][-1] = max(merge_intervals[-1][-1], interval[1])


        return merge_intervals
        
