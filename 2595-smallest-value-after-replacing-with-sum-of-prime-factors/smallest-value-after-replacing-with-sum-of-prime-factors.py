class Solution:
    def smallestValue(self, n: int) -> int:
        def sum_of_primes(x):
            if x <= 1:
                return x
            s = 0
            while x % 2 == 0:
                s += 2
                x //= 2
            f = 3
            while f * f <= x:
                while x % f == 0:
                    s += f
                    x //= f
                f += 2
            if x > 1:
                s += x
            return s
        while True:
            nxt = sum_of_primes(n)
            if n == nxt:
                return n
            n = nxt 
        
        