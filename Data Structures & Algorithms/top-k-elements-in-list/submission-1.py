class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        array = [[] for i in range(len(nums)+1)]

        for num in nums:
            if num in freq:
                freq[num] +=1

            else:
                freq[num] = 1
        
        for n,c in freq.items():
            array[c].append(n)

        res = []
        for i in range(len(array) -1, 0 , -1):
            for j in array[i]:
                res.append(j)
                if len(res) == k:
                    return res

        