class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        for i in range(n):
            nums1[m+i] = nums2[index]
            index+=1
            
        print(nums1)
        
        nums1.sort()
        
        return nums1
