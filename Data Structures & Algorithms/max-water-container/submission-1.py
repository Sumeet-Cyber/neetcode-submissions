class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        vol_m = 0
        while l < r:
            vol = (r-l) * min(heights[r], heights[l])
            if vol > vol_m: vol_m = vol
            if heights[l] <= heights[r]: l += 1
            elif heights[l] > heights[r]: r -= 1
        return vol_m