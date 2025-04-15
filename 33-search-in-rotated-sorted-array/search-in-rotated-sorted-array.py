class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(lo, hi):
            if len(nums) == 1:
                return 0

            if nums[lo] < nums[hi]:
                return 0 
            while lo<=hi:
                mid = (lo + hi) // 2
                if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                    return mid + 1
                elif nums[mid] >= nums[lo]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1
        def normal_binary(lo, hi):
            while lo<= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1
        
        rotation_index = binary_search(0, len(nums) - 1)

        if nums[rotation_index] <= target <= nums[-1]:
            return normal_binary(rotation_index,  len(nums)-1) 
        return normal_binary(0, rotation_index -1)
        