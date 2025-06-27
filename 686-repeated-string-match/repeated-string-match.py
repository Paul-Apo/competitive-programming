class Solution:
    def repeatedStringMatch(self, a, b):
        if not b:
            return 0
        min_repeats = (len(b) + len(a) - 1) // len(a)        
        repeated = a * min_repeats
        if b in repeated:
            return min_repeats        
        repeated += a
        if b in repeated:
            return min_repeats + 1
        

        return -1