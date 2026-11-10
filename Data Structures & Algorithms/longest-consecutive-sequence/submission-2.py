class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        s = set(nums)
        l = l_m = 0
        for num in s:
            if num-1 not in s:
                l = 1
                while num + l in s:
                    l += 1
            l_m = max(l, l_m)

        return l_m