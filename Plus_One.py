class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
         
        digits = [str(i) for i in digits]
        str1 = "".join(digits)
        integer = int(str1)
        integer+=1
        str2 = str(integer)
        list1 = list(str2)
        list1 = [int(i) for i in list1]
        
        return list1