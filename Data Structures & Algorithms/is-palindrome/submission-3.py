class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        f, l = 0, len(s) - 1
        while f <= l:
            if not s[f].isalnum():
                f += 1
                continue
            if not s[l].isalnum():
                l -= 1
                continue
            if s[f] != s[l]:
                return False
            f += 1
            l -= 1
        return True