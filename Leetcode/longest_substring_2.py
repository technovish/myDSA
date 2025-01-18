class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == ' ':
            return 1
        x = list(s)
        if len(x) == 1:
            return 1
        str =''
        new = []
        sbstrs = []
        for i in range(len(x)):
            if x[i] != x[i-1] and x[i] not in new:
                new.append(x[i])
                #new.append(x[i+1])
                str += x[i]
                #str += x[i+1]
            else:
                new=[]
                new.append(x[i])
                sbstrs.append(str)
                str =''
                str += x[i]
                continue
        sbstrs.append(str)
        lst = sbstrs
        chars = 0
        for i in range(len(lst)):
            if chars < len(lst[i]):
                chars = len(lst[i])
        return chars
       


