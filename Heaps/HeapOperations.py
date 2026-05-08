# if you start with empty lists and only use heapq operations.

# Why heapify isn’t needed here
# heapq.heapify(lst) is for when you already have an arbitrary list of values and you want to transform it into a heap in-place. In the article’s pattern, min_heap and # max_heap start empty, e.g.:
self.min_heap = []
self.max_heap = []
Then you only modify them via:

heappush(...)
heappop(...)
heappushpop(...)
# These functions maintain the heap invariant automatically, so there’s nothing to “heapify”.

# When you would need heapify
# If you did something like this (direct list assignment / appending without heappush):

self.min_heap = [5, 1, 9]   # arbitrary order
# then you should call:

heapq.heapify(self.min_heap)
# But for the two-heaps median approach in the article, you typically never build the heaps that way—so heapify is unnecessary.
