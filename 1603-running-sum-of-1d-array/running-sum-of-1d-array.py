class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        counter = 0
        new_list = []
        for i in nums:
            counter = i + counter
            new_list.append(counter)
        return new_list
        