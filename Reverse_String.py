class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s) - 1
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[length]
            s[length] = temp
            length -= 1
        return s