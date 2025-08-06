class Solution:
    def longestPalindrome(self, s: str) -> str:
        resL = 0
        resR = 0
        resLen = 0
        for i in range(len(s)):
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resL = l
                    resR = r
                    resLen = r - l + 1
                l = l - 1
                r = r + 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resL = l
                    resR = r
                    resLen = r - l + 1
                l = l - 1
                r = r + 1                
        return s[resL: resR+ 1]

    
        
        
     
            