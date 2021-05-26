class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(10):
            num_str = str(n)
            lst = list(num_str)
            lst = [int(x) for x in lst]
            
            lst = [x**2 for x in lst]
            y = sum(lst)
            if y == 1:
                return True
            n = int(y)
        
        return False