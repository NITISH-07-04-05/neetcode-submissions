class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        output = []
        while k != 0:
            value = heapq.heappop(nums)
            output.append(-value)
            k -=1
        return output
            