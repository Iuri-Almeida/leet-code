class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = []
        for i in s:
            if i in '{[(':
                p.append(i)
            else:
                if p:
                    t = p.pop()
                    if (t + i) not in '{}[]()':
                        return False
                else:
                    return False
        return True if not p else False