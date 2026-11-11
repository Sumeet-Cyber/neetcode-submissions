class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        def b_s(t, i):
            l, r = i+1, n
            while l < r:
                mid = (l + r) // 2
                if t < numbers[mid]:
                    r = mid
                if t > numbers[mid]:
                    l = mid + 1
                if t == numbers[mid]:
                    return mid
            return -1

        for i in range(n):
            temp = target - numbers[i]
            j = b_s(temp, i)
            if j != -1:
                return [i+1, j+1]