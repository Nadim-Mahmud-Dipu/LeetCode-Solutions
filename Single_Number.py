from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        x_dict = Counter(nums)
        
        return list(x_dict.keys())[list(x_dict.values()).index(1)]
        