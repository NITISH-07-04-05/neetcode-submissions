class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        array = [[]for i in range(len(nums)+1)]
        output = []
        for num,freq in hashmap.items():
            array[freq].append(num)

        for i in range(len(array)-1, -1 ,-1):
            for num in array[i]:
                output.append(num)

                if len(output) == k:
                    return output