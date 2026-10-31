class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sa = list([0]) * 26
        ta = list([0]) * 26
        for i in range(len(s)):
            sa[ord(s[i]) - 97] += 1
            ta[ord(t[i]) - 97] += 1
        for i in range(26):
            if sa[i] != ta[i]:
                return False
        return True