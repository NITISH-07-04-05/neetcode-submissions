class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def spread(left,right):
            value = 0
            while left >=  0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                value +=1
            return value



        for i in range(len(s)):
            odd = spread(i,i)
            even = spread(i,i+1)

            count = count + odd + even

        return count
            