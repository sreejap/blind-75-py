class MedianFinder:
    # https://algo.monster/liteproblems/295#pitfalls
    def __init__(self):
        self.min_heap = []
        self.max_heap = []


    def addNum(self, num: int) -> None:
        heapq.heappush (self.min_heap, -heappushpop (self.max_heap, -num)) # add negative of number to max heap ... and then pop that add to min heap

        if len (self.min_heap) - len (self.max_heap) > 1:
            heapq.heappush (self.max_heap, -heappop (self.min_heap))

    def findMedian(self) -> float:

        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2.0 #make sure to negate the value from max heap

        return float(self.min_heap[0])        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
