class Solution:
    def binary_search(self, lo,hi, condition):
        while lo <= hi:
            mid = (hi + lo ) // 2
            result = condition(mid)
            if result == "found":
                return mid
            elif result == "left":
                hi = mid - 1
            elif result == "right":
                lo = mid + 1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        def condition(mid):
            if nums[mid] == target:
                if mid-1 >= 0 and nums[mid -1] == target:
                    return "left"
                else:
                    return "found"
            elif nums[mid] > target: 
                return "left"
            elif nums[mid] < target:
                return "right"
        return self.binary_search(0, len(nums)-1, condition)
    
   
        
