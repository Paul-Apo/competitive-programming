class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        concat = ""
        rev = ""
        for strin in s:
            if strin.isalnum():
                concat += strin
        for i in range(len(concat)-1,-1,-1):
            rev += concat[i]
        if rev == concat:
            return True
        else:
            return False
        