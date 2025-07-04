class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        n = len(words)
        prefix = [0] * (n + 1)
        for i in range(n):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        result = []
        for li, ri in queries:
            count = prefix[ri + 1] - prefix[li]
            result.append(count)
        
        return result
