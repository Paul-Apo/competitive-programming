class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        isPrime = [1] * n
        isPrime[1] = isPrime[0] = 0
        for i in range(2, int(n**0.5)+1):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = 0
        return sum(isPrime)
        