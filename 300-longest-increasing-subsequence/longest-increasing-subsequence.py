class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[i] stores the smallest value that ends an increasing subsequence of length i+1
        tails = []
        
        for num in nums:
            # Use binary search to find the position to insert num
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            # If we're at the end, append the number
            if left == len(tails):
                tails.append(num)
            # Otherwise, replace the number at position left
            else:
                tails[left] = num
                
        return len(tails)
        