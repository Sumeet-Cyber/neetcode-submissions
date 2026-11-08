class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        mul = 1
        z_c, z_i = 0, -1
        for i in range(len(nums)):
            if nums[i] != 0:
                mul *= nums[i]
            else:
                z_c += 1
                z_i = i
            if z_c > 1:
                break
        arr = [0] * len(nums)
        if z_c > 1:
            return arr
        elif z_c == 1:
            arr[z_i] = mul
        elif z_c == 0:
            for i in range(len(nums)):
                arr[i] = mul // nums[i]

        return arr