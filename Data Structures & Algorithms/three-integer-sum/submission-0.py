class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            num = nums[i]
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                temp = num + nums[l] + nums[r]
                if temp > 0: r -= 1
                if temp < 0: l += 1
                if temp == 0: 
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return ans
