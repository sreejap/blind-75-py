class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack (start,rem,path):
            if rem == 0:
                results.append (list(path))
                return results
            elif rem < 0:
                return

            for i in range (start,len(candidates)):
                ans = rem - candidates [i]
                path.append (candidates[i])
                backtrack (i,ans,path)
                path.pop()


        backtrack (0,target,[])    
        return results
