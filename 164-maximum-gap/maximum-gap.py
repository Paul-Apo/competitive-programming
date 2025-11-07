class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        mn = min(nums)
        mx = max(nums)
        if n < 2:
            return 0
        if mn == mx:
            return 0
        bucket_size = max(1, (mx -mn) // (n -1))
        bucket_count = (mx - mn) // bucket_size + 1

        bucket_min = [float("inf")] * bucket_count
        bucket_max = [float("-inf")] * bucket_count

        for num in nums:
            index = (num - mn) // bucket_size
            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)
        pre_max = mn
        max_gap = 0
        for i in range(bucket_count):
            if bucket_min[i] == float("inf"):
                continue
            max_gap = max(max_gap, bucket_min[i] - pre_max)
            pre_max = bucket_max[i]
        return max_gap

