class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        n = len(nums)
        ans = 0
        
        for i in range(n):
            curr = 1
            for j in range(i, n):
                # If nums[j] cannot be part of any LCM=k subarray, stop early
                if k % nums[j] != 0:
                    break
                
                curr = lcm(curr, nums[j])
                
                if curr == k:
                    ans += 1
                elif curr > k:
                    break
        
        return ans
        