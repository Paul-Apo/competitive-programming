class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        score_map = {}
        for i, s in enumerate(sorted_score):
            if i == 0:
                score_map[s] = "Gold Medal"
            elif i == 1:
                score_map[s] = "Silver Medal"
            elif i == 2:
                score_map[s] = "Bronze Medal"
            else:
                score_map[s] = str(i + 1)
        return [score_map[i] for i in score ]
            
        