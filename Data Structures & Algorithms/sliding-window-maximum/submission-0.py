class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k-1

        curr_max = max(nums[:k])
        output = []
        output.append(curr_max)
        while right < len(nums):
            local_max = curr_max
            if nums[left] == curr_max:
                local_max = max(nums[left:right+1])
            if right != len(nums):
                if nums[right+1] < nums[left]:
                    local_max = curr_max

            output.append(local_max)
            left+=1
            right+=1
        return output