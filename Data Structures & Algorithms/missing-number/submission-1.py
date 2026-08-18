class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0

        for num in range(len(nums)+1):
            if num < len(nums):
                result ^= nums[num]
            result ^= num

        return result