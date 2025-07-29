class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(idx, memo):
            if idx >= len(nums):
                return 0
            
            if idx not in memo:
                leave = dp(idx + 1, memo)
                rob = nums[idx] + dp(idx + 2, memo)
                memo[idx] = max(leave, rob)
            
            return memo[idx]
        
        return dp(0, {})

        