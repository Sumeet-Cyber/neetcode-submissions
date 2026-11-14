class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, mp, ans = 0, dict(), 0
        for i, num in enumerate(s):
            if num in mp:
                l = max(mp[s[i]] + 1, l)
            mp[num] = i
            ans = max(ans, i - l + 1)
        return ans