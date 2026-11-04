class Solution:

    def encode(self, strs: List[str]) -> str:
        prefix = ''
        num = 0
        cnt = 0
        for word in strs:
            num += len(word)
            prefix += str(num) + '_'
            cnt += 1
        prefix += str(cnt)
        t = ''.join(strs) + '_' + prefix

        # print(t)
        return t
    
    def decode(self, s: str) -> List[str]:

        *packet, cnt = s.split('_')
        cnt = int(cnt)

        # cnt = int(s[-1])
        if cnt == 0:
            return []
        ans = []
        # pref = list(map(int, s.split('_')[-cnt-1:-1]))
        # word, pref, end = s.split('_')
        pref = packet[-cnt:]
        strs = '_'.join(packet[:-cnt])
        # print(pref)
        # print(strs)
        s, e = 0, 0
        for i in range(len(pref)):
            ans.append(strs[s:int(pref[e])])
            s = int(pref[e])
            e += 1
        return ans