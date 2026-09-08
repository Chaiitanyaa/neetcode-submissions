class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        print(stones)
        while len(stones) >= 2:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if stone1 > stone2:
                new_weight = stone1 - stone2
                heapq.heappush_max(stones,new_weight )
            else:
                new_weight = stone2 - stone1
                heapq.heappush_max(stones,new_weight )
        return stones[0]