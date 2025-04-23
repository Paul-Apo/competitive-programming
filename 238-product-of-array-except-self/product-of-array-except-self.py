class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mul = 1
        r_mul = 1
        n = len(nums)
        o = [1] * n
        for i in range(n):
            j = -i-1
            o[i] = l_mul
            l_mul *= nums[i]
        for j in range(n-1, -1, -1):
            o[j] *= r_mul
            r_mul*= nums[j]
        return [r for r in o]

        