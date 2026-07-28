class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0 
        high = len(numbers) - 1

        while low < high:
            value = numbers[low] + numbers[high]
            if value == target:
                return [low+1,high+1]

            if value > target:
                high -= 1

            if value < target:
                low += 1

            
