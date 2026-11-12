class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0]*26
        for i in range(0,len(s)):
            target_s = ord(s[i]) - ord('a')
            target_t = ord(t[i]) - ord('a')
            counts[target_s] +=1
            counts[target_t] -=1
        return all(c == 0 for c in counts)