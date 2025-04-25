class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_close = {")": "(", "}": "{", "]":"["}
        for c in s:
            if c in open_close:
                if stack and stack[-1] == open_close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            