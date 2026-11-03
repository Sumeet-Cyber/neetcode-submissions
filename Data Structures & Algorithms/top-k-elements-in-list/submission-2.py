class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        ans_dict = defaultdict(int)

        for num in nums:
            ans_dict[num] += 1
        for key in ans_dict:
            ans.append([ans_dict[key], key])
        # print(ans)
        # temp = lambda t: t[0]
        ans.sort()
        # print(ans)
        j = [x[1] for x in ans[len(ans)-k:]]
        # print(j)
        return j