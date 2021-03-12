
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        string = ""
        for i in range(len(strs[0])):
            string += strs[0][i]
            ans = True
            for j in strs:
                if j[:i+1] == string:
                    pass
                else:
                    return string[:-1]
        return string
        