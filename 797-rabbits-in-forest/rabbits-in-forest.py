class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = 0
        count = Counter(answers)

        for x, freq in count.items():
            group_size = x + 1
            group = math.ceil(freq / group_size)
            total += group * group_size
        return total