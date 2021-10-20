class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in set(t):
            if t.count(i) != s.count(i) or len(s) != len(t): return False
        return True