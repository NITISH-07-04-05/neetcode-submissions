class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_value = nums[0]
        min_value = nums[0]

        answer = max_value

        for i in range(1,len(nums)):
            x = nums[i]

            prev_max = max_value
            prev_min = min_value

            max_value = max(x,x*prev_max,x*prev_min)
            min_value = min(x,x*prev_max,x*prev_min)

            answer = max(answer,max_value)

        return answer