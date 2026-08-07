class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,num in enumerate(nums):
            value = target - num

            if value in hashmap:
                return [hashmap[value],index]

            else:
                hashmap[num] = index

        return []
        