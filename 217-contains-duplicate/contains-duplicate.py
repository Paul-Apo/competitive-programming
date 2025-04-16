class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        exists = set()
        for i in range(0, len(nums)):
            if nums[i] in exists:
                return True
            else:
                exists.add(nums[i])
        return False
        