class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) == 1:
            return ""
        nice_strings = []
        strings = [s[i: j] for i in range(len(s))
           for j in range(i + 1, len(s) + 1)]

        for y in strings:
            set1 = set(list(y))
            flag = False

            for i in set1:
                if (i.lower() in set1) and (i.upper() in set1) and len(y) != 1:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                nice_strings.append(y)

        if len(nice_strings) == 1:
            return nice_strings[0]
        elif len(nice_strings) == 0:
            return ""
        else:
            return max(nice_strings,key=len)
        
        