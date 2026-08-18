class Solution:
    def reverse(self, x: int) -> int:
        result = 0

        is_Negative = False
        if x < 0:
            is_Negative = True
            x = -x
        while x != 0:
            digit = x % 10
            result += digit
            x //=10
            if x <=0:
                break
            result *= 10

        if result > 2**31 - 1 or result < -2**31:
            return 0

        if is_Negative == True:
            return -result

        else:
            return result