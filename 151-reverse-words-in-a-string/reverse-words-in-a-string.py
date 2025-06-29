class Solution:
    def reverseWords(self, s: str) -> str:
        wrdList = list(s.split(" "))
        resutlstr = ""
        for i in range(len(wrdList)-1, -1,-1):
            if wrdList[i] == '':
                print(i)
                continue
            resutlstr += wrdList[i] + " "
        return resutlstr.strip()
        