from heapq import heapify, heappop
def heap_top_3(arr: list[int]) -> list[int]:
    res = []
    heapify(arr) # It rearranges the list arr in-place into a heap — specifically, a min-heap.
    for _ in range(3):
        res.append(heappop(arr))
    return res

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = heap_top_3(arr)
    print(" ".join(map(str, res)))
