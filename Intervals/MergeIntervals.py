class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals first and then do the merge

        merged = []

        intervals.sort (key=lambda x:x[0])

        for i in intervals:
            if not merged or merged [-1][1] < i[0]:
                merged.append (i)
            
            else:
                # merged[-1][0] = min (merged[-1][0], i[0]) This step is not needed
                merged[-1][1] = max (merged[-1][1], i[1])

        return merged
