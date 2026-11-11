class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        f, l = 0, len(s) - 1
        while f <= l:
            while f < l and not s[f].isalnum():
                f += 1
            while f < l and not s[l].isalnum():
                l -= 1
            if s[f] != s[l]:
                return False
            l -= 1
            f += 1
        return True