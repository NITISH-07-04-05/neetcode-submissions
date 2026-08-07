class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            sortedS = ''.join(sorted(s))

            if not sortedS in res:
                res[sortedS] = []

            res[sortedS].append(s)

        return list(res.values())

        