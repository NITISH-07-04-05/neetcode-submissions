class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            diff = first - second

            if diff != 0:
                heapq.heappush(stones,-diff)

        if not stones[0]:
            return 0 
        else:
            return -stones[0]