class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unq_nums = set(nums)
        longest = 0

        for i in unq_nums:
            if i-1 not in unq_nums: 
                next_num = i
                length = 1
                while next_num+1 in unq_nums: 
                    next_num += 1
                    length += 1

                longest = max(longest,length) 
        return longest


        