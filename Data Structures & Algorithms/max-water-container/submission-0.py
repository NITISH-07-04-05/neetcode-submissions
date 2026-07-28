class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low = 0 
        high = len(heights) - 1
        max_value = 0
        while low < high:
            value = (high-low)*min(heights[low],heights[high])
            max_value = max(value,max_value)

            if heights[low] < heights[high]:
                low += 1

            else:
                high -= 1
        return max_value