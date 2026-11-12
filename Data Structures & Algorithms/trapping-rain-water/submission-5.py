class Solution:
    def trap(self, height: List[int]) -> int:
        # if len(height) < 3: return 0
        n = len(height)
        vol = 0
        l, r = 0, n-1
        left_max_height, right_max_height = height[l], height[r]
        while l < r:
            if left_max_height <= right_max_height:
                l += 1
                left_max_height = max(left_max_height, height[l])
                vol += left_max_height - height[l]
            else:
                r -= 1
                right_max_height = max(right_max_height, height[r])
                vol += right_max_height - height[r]
            # print(vol)
        return vol
