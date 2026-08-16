class Solution:
    def countSubstrings(self, s: str) -> int:
        if s is None:
            return 0
        count = 0
        def spread(left, right):
            val = 0
            while left >= 0 and right <len(s) and s[left] == s[right]:
                val += 1
                left -= 1
                right += 1

            return val
            
        for i in range(len(s)):
            odd = spread(i,i)
            even = spread(i,i+1)
            count = count + odd + even

        return count 
            