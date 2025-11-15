class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Store (start, original index)
        starts = sorted((intervals[i][0], i) for i in range(n))
        start_values = [s[0] for s in starts]
        
        result = [-1] * n
        
        for i, (start, end) in enumerate(intervals):
            # Binary search for smallest start >= end
            pos = bisect_left(start_values, end)
            if pos < n:
                result[i] = starts[pos][1]
        
        return result

        