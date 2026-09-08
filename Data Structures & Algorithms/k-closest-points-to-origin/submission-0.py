class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        results = []
        for x,y in points:
            dist = x**2 + y**2
            heapq.heappush(minHeap, [dist, x, y])

        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            results.append([x,y])

        return results

            
