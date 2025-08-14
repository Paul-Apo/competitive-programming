class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        val = lambda c: ord(c) - ord('a') + 1
        p_k = pow(power, k, modulo)    
        cur_hash = 0
        res_index = n - k    
        for i in range(n - 1, -1, -1):
            cur_hash = (cur_hash * power + val(s[i])) % modulo
            if i + k < n:
                cur_hash = (cur_hash - val(s[i + k]) * p_k) % modulo
            if i + k <= n and cur_hash == hashValue:
                res_index = i    
        return s[res_index: res_index + k]
        