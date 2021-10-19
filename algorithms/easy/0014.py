class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        r = strs.pop(0)
        c = 0
        while r:
            for s in strs:
                if r in s:
                    if r.index(r) == s.index(r):
                        c += 1
            if c == len(strs):
                return r
            r = r[:-1]
            c = 0
        return r
