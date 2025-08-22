class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        count = [0] * 26
        curr_len = 1
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or (s[i - 1] == 'z' and s[i] == 'a')):
            
                curr_len += 1
            else:
                curr_len = 1
            count[ord(s[i]) - ord('a')] = max(curr_len, count[ord(s[i]) - ord('a')])
        return sum(count)