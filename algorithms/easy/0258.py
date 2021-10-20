class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        while len(num) != 1:
            n = 0
            for i in num:
                n += int(i)
            num = str(n)
        return int(num)

x = Solution()
print(x.addDigits(1234))