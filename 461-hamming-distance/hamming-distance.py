class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        while xor:
            xor &= xor - 1  # remove the lowest set bit
            count += 1
        return count