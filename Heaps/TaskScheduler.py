# https://leetcode.com/problems/task-scheduler/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0]*26
        for t in tasks:
            freq [ord(t) - ord('A')] += 1
        
        # make the pq
        pq = [-f for f in freq if f >0] # it is important to skip the zeros
        heapq.heapify(pq)

        time = 0
        while pq:
            cycle = n+1
            temp_store = []
            count = 0
            while cycle > 0 and pq:
                # we only run until we have atleast n intervals gap
                # we put the max freq in max heap so that we can use those tasks more
                next_freq = -heapq.heappop(pq)
                if next_freq > 1:
                    temp_store.append (next_freq-1)
                cycle -=1
                count += 1
            
            for x in temp_store:
                heapq.heappush(pq,-x)
            
            time += count if not pq else n+1 # if pq is empty add the count , otherwise add the interval gap
        return time
