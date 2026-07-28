class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        n = len(nums)
        for low in range(n):

            if low > 0 and nums[low] == nums[low-1]:
                continue
            mid = low + 1
            high = len(nums) - 1
            while mid < high :
                value = nums[low] + nums[mid] + nums[high]
                if value == 0:
                    output.append([nums[low],nums[mid],nums[high]])
                    mid +=1
                    high -=1
                    while mid < high and nums[mid] == nums[mid+1]:
                        mid += 1


                if value < 0:
                    mid +=1
                
                if value > 0:
                    high -=1

        return output