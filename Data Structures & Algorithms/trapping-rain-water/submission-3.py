class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        n = len(height)
        vol = 0
        mnh = [0] * n
        mxh = [0] * n
        mn, mx = height[0], height[-1]
        for i in range(n):
            if height[i] > mn:
                mn = height[i]
            if height[n -1 -i] > mx:
                mx = height[n-1-i]
            mnh[i] = mn
            mxh[n-1-i] = mx
        # print(mnh, mxh)
        for i in range(n):
            vol += max(0, min(mnh[i], mxh[i]) - height[i])
        
        return vol
