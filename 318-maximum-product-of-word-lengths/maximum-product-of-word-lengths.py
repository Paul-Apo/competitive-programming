class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lengths = [len(w) for w in words]

        # build bitmask for each word
        for i, word in enumerate(words):
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            masks[i] = mask

        max_product = 0
        # compare pairs
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:  # no common letters
                    max_product = max(max_product, lengths[i] * lengths[j])
        return max_product
        