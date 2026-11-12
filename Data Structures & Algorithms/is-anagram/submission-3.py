class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] +=1
            if i not in s_dict:
                s_dict[i] = 1
        
        for j in t:
            if j in t_dict:
                t_dict[j] +=1
            if j not in t_dict:
                t_dict[j] = 1

        counts_s = dict(Counter(s))
        counts_t = dict(Counter(t))
        
        return counts_s == counts_t