from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a_dict = Counter(nums)

        for key in a_dict.keys():
            if a_dict[key] > (len(nums) // 2):
                return key