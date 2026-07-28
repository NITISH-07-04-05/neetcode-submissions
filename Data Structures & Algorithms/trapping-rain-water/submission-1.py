class Solution:
    def trap(self, height: List[int]) -> int:
        left_max,right_max = 0,0
        left,right = 0,len(height) - 1
        water_trapped = 0
        while left <= right:
            left_max = max(height[left],left_max)
            right_max = max(height[right],right_max)
            
            if left_max < right_max:
                water_trapped += left_max - height[left]
                left += 1

            else:
                water_trapped += right_max - height[right]
                right -=1
        return water_trapped