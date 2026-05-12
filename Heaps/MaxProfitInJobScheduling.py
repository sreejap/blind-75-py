# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
from heapq import heappush, heappop
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime,endTime,profit))

        max_profit = 0
        heap = []

        for start, end, profit in jobs:
            while heap and start >= heap[0][0]:
                max_profit = max (max_profit, heap[0][1])
                heappop(heap)

            combined_job = (end, profit+max_profit)
            heappush (heap, combined_job)
        
        while heap:
            max_profit = max (max_profit, heap[0][1])
            heappop (heap)

        return max_profit
