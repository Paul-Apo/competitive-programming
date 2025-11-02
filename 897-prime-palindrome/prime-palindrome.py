class Solution:
    def primePalindrome(self, n: int) -> int:
        if n <= 2: return 2
        if n <= 3: return 3
        if n <= 5: return 5
        if n <= 7: return 7
        if n <= 11: return 11

        def is_prime(x: int) -> bool:
            if x < 2: return False
            if x == 2 or x == 3: return True
            if x % 2 == 0 or x % 3 == 0: return False
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0: return False
                i += 6
            return True

        def build_palindrome(root: int, even: bool) -> int:
            s = str(root)
            if even:
                return int(s + s[::-1])
            else:
                return int(s + s[-2::-1])   # skip the last digit of root

        # find a starting root whose palindrome >= n
        root = 1
        while build_palindrome(root, True) < n:
            root += 1

        while True:
            # even length
            pal = build_palindrome(root, True)
            if pal >= n and is_prime(pal):
                return pal
            # odd length
            pal = build_palindrome(root, False)
            if pal >= n and is_prime(pal):
                return pal
            root += 1