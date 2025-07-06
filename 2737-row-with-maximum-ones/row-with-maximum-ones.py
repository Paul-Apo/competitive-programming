class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = -1
        row_index = -1
        
        for i, row in enumerate(mat):
            count_ones = sum(row)
            if count_ones > max_ones:
                max_ones = count_ones
                row_index = i
                
        return [row_index, max_ones]

        