class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small = []
        large = []
        d = 1
        while d * d <= n:
            if n % d == 0:
                small.append(d)
                if d != n // d:
                    large.append(n // d)
            d += 1
        
        total_length = len(small) + len(large)
        if k > total_length:
            return -1
        
        if k <= len(small):
            return small[k -1]
        else:
            index_range = k - len(small) - 1
            return large[::-1][index_range]
        

        