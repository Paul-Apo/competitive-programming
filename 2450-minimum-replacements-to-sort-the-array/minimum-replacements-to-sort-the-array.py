class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0
        upper = nums[n - 1]  # Initialize upper bound with the last element
        
        # Iterate from second-to-last element to the first
        for i in range(n - 2, -1, -1):
            if nums[i] <= upper:
                # If current element is valid, update upper bound
                upper = nums[i]
                continue
            # Calculate number of parts to split nums[i] into
            parts = (nums[i] + upper - 1) // upper  # Ceiling of nums[i] / upper
            operations += parts - 1  # Number of operations is parts - 1
            # Update upper bound to the smallest possible value after splitting
            upper = nums[i] // parts
        
        return operations
        