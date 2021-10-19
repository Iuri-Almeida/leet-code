class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        while x[-1] == '0' and len(x) > 1:
            x = x[:-1]
        x = x[-1:-(len(x) + 1):-1]
        if x[-1] == '-':
            x = x[:-1]
            x = '-' + x
        x = int(x)
        return x if (-2**31) <= x <= (2**31 - 1) else 0
