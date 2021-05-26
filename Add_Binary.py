class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)
        sum = bin(x+y)
        answer = sum[2:]
        return answer