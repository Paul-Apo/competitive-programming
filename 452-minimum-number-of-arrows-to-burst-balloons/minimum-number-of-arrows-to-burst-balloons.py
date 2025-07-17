class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 1
        prev = points[0]
        for i in range(1, len(points)):
            curr = points[i]
            if prev[1] >= curr[0]:
                prev = [curr[0], min(prev[1], curr[1])]
            else:
                count += 1
                prev = curr 
        return count
        