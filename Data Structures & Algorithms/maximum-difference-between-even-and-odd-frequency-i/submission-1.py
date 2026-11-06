class Solution:
    def maxDifference(self, s: str) -> int:
        alpha = [0] * 26
        for l in s:
            alpha[ord(l)-97] += 1
        
        mx_o, mn_e = 1, float('inf')
        for i in range(26):
            if alpha[i]:
                if alpha[i] % 2 == 0:
                    if alpha[i] < mn_e:
                        mn_e = alpha[i]
                else:
                    if alpha[i] > mx_o:
                        mx_o = alpha[i]
        return mx_o - mn_e