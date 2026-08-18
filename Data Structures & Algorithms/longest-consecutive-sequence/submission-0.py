class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        total = 0
        for i in nums:
            if i-1 in nums:
                continue
            else:
                temp = i
                count = 0
                while temp in nums:
                    count +=1
                    temp = temp + 1
                total = max(total,count)

        return total