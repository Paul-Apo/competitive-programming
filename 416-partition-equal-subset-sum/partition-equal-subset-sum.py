class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if(sum(nums) % 2):
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) / 2
        for i in range(len(nums) -1, -1, -1):
            nextDp = dp.copy()
            for t in dp:
                nextDp.add(t + nums[i])
            dp = nextDp
        return True if target in nextDp else False


        