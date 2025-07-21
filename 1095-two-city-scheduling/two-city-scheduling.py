class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for a, b in costs:
            diff.append([b-a, a, b])
        res = 0
        diff.sort()
        for i in range(len(costs)):
            if i < len(diff) // 2:
                res += diff[i][2]
            else:
                res += diff[i][1]
        return res

        