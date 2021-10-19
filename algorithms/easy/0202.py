class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = []
        while n != 1 and l.count(n) <= 1:
            x = str(n)
            n = 0
            for i in x:
                n += int(i) ** 2
            l.append(n)
        return n == 1
