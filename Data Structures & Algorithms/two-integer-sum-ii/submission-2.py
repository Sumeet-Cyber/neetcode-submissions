class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1
        while l < r:
            sugar = numbers[l] + numbers[r]
            if target < sugar:
                r -= 1
            elif target >  sugar:
                l += 1
            elif target == sugar:
                return [l+1, r + 1]