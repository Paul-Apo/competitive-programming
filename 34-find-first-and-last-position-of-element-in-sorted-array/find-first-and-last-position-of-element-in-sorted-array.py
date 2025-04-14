class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(lo, hi, find_left):
            res = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    res = mid
                    if find_left:
                        hi = mid - 1 
                    else:
                        lo = mid + 1 
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return res
        first = binary_search(0, len(nums) - 1, find_left=True)        
        if first == -1:
            return [-1, -1]        
        last = binary_search(0, len(nums) - 1, find_left=False)
        return [first, last]


        

        