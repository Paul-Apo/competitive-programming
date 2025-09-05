class Solution(object):
    def singleNumber(self, nums):
        xor_all = 0
        for num in nums:
            xor_all ^= num
        mask = xor_all & -xor_all
        a, b = 0, 0
        for num in nums:
            if (num & mask):
                a ^= num
            else:
                b ^= num
        return [a, b]
        