class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for i in range(32):
            bit_sum = 0
            for n in nums:
                bit_sum += (n >> i) & 1
            res = res | (bit_sum % 3) << i
        if res >= (1 << 31):
            res -= (1 << 32)
        return res

        