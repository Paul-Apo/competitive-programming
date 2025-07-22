class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negNums = []
        for num in nums:
            num = -1 * num
            negNums.append(num)
        heapq.heapify(negNums)
        for i in range(k -1):
            heapq.heappop(negNums)
        return (heapq.heappop(negNums))* -1