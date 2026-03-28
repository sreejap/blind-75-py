from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for p in points:
            x,y = p
            heappush(heap,(x*x+y*y ,[x,y]))
        
        for i in range(k):
            _,pt = heappop(heap)            
            res.append (pt)
                    
        return res
