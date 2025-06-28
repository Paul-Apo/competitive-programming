class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Sum of each subarray of length k
        sum_k = [0] * (n - k + 1)
        window_sum = sum(nums[:k])
        sum_k[0] = window_sum
        for i in range(1, n - k + 1):
            window_sum += nums[i + k - 1] - nums[i - 1]
            sum_k[i] = window_sum

        # Best left index for each position
        left = [0] * len(sum_k)
        best = 0
        for i in range(len(sum_k)):
            if sum_k[i] > sum_k[best]:
                best = i
            left[i] = best

        # Best right index for each position
        right = [0] * len(sum_k)
        best = len(sum_k) - 1
        for i in range(len(sum_k) - 1, -1, -1):
            if sum_k[i] >= sum_k[best]:
                best = i
            right[i] = best

        # Now, pick middle subarray and find max total using left and right
        max_total = 0
        res = []
        for j in range(k, len(sum_k) - k):
            i = left[j - k]
            m = j
            r = right[j + k]
            total = sum_k[i] + sum_k[m] + sum_k[r]
            if total > max_total:
                max_total = total
                res = [i, m, r]

        return res
        