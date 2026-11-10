class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        ans = 0

        for num in nums:
            if not hmap[num]:
                hmap[num] = hmap[num-1] + hmap[num+1] + 1
                hmap[num - hmap[num-1]] = hmap[num]
                hmap[num + hmap[num+1]] = hmap[num]
            ans = max(ans, hmap[num])
        return ans
                