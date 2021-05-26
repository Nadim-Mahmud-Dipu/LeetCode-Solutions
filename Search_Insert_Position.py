class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        position = 0
        if len(nums) == 1:
            if target<nums[0]:
                return 0
            elif target>nums[0]:
                return 1
        if target in nums:
            position = nums.index(target)
        else:   
            for i in range(len(nums) - 1):
                if target > nums[i] and target < nums[i + 1]:
                    position = i+1
                elif target<nums[0]:
                    return 0
                elif target>nums[len(nums)-1]:
                    return len(nums)
        return position