class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]
        if n == 0:
            return output

        def count(number):
            value = 0
            while number:
                number &= number - 1
                value+=1

            return value

        for num in range(1,n+1):
            value = count(num)
            output.append(value)

        return output