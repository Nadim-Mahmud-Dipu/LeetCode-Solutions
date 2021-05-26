class Solution:

    def climbStairs(self, n: int) -> int:
        temp = 0
        res = [1]

        for i in range(1, n + 1):
            s = i - 3
            e = i - 1
            if s >= 0:
                temp -= res[s]
            temp += res[e]
            res.append(temp)

        return res[n]