class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            Sorted = "".join(sorted(word))

            if Sorted in hashmap:
                hashmap[Sorted].append(word)

            else:
                hashmap[Sorted] = [word]

        return [word for word in hashmap.values()]