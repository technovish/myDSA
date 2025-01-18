class Solution(object):
    def lengthOfLongestSubstring(self, s):
        x = list(s)
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
                new.remove(x[i])
                new.append(x[i])
                sbstrs.append(str)
                str =''
                str += x[i]
                continue
        sbstrs.append(str)
        return sbstrs
    def check_count(self,lst):
        chars = 0
        for i in range(len(lst)):
            if chars < len(lst[i]):
                chars = len(lst[i])
        return chars





ls = Solution()
chk_lst = ls.lengthOfLongestSubstring('dvdf')
counts = ls.check_count(chk_lst)
print(chk_lst)
print(counts)

ls1 = ls
ls1.lengthOfLongestSubstring('pwwkew')
