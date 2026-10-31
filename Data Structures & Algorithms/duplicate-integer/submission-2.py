class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0: return False
        s = set()
        s.add(nums[0])
        for num in nums[1:]:
            if num in s:
                return True
            s.add(num)
        return False
        