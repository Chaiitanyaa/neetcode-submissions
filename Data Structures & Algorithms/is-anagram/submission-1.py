class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        elemS = {}
        elemT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in elemS:
                elemS[s[i]] += 1
            else:
                elemS[s[i]] = 1

        for i in range(len(t)):
            if t[i] in elemT:
                elemT[t[i]] += 1
            else:
                elemT[t[i]] = 1


        return elemS == elemT
            