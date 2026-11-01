class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashD = dict()
        for i in range(len(nums)):
            if target - nums[i] in hashD:
                return [hashD[target - nums[i]], i]
            else:
                hashD[nums[i]] = i
            # print(f'new hash: {hashD}')