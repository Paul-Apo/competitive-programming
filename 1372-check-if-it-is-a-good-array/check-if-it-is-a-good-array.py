class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        g = nums[0]
        for v in nums[1:]:
            g = gcd(g, v)
        return g == 1