class Solution:
    def twoSum(self,numbers, target: int):
        for i, num in enumerate(numbers):
            diff = target - num
            # Perform binary search for 'diff'
            l, r = 0, len(numbers) - 1
            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == diff:
                    # Ensure we don't use the same index twice
                    if i != mid:
                        return [i + 1, mid + 1] if i < mid else [mid + 1, i + 1]
                    else:
                        # Check if there's another occurrence of 'diff'
                        # Search to the left
                        if mid > 0 and numbers[mid - 1] == diff:
                            return [i + 1, mid]
                        # Search to the right
                        if mid + 1 < len(numbers) and numbers[mid + 1] == diff:
                            return [i + 1, mid + 2]
                        break
                elif diff > numbers[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return [-1]

            