class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        out1 = {}
        out2 = {}
        for i in range(len(s)):
            if s[i] not in out1:
                out1[s[i]] = 0
            else:
                out1[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in out2:
                out2[t[i]] = 0
            else:
                out2[t[i]] += 1
        if out1 == out2:
            return True
        return False

