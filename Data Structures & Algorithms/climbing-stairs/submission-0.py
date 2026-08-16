class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 2

        for _ in range(3,n+1):
            one ,two = two , two+one

        return two