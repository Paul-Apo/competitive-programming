class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        if len(s) < 2:
            return s

        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            l1 = self.expandAroundCenter(s, i, i)
            # Even length palindrome
            l2 = self.expandAroundCenter(s, i, i + 1)
            
            if len(l1) > len(longest):
                longest = l1
            if len(l2) > len(longest):
                longest = l2

        return longest

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Return the substring from the updated left and right pointers
        return s[left + 1 : right]
            