class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        jj = lambda x: len(x)
        strs.sort(key = jj)
        ans  = defaultdict(list)
        for iword in range(len(strs)):
            temp = [0 for x in range(26)]
            for letter in strs[iword]:
                temp[ord(letter)-97] += 1
            ans[tuple(temp)].append(strs[iword])

        return list(ans.values())