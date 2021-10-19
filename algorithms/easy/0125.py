class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(list(filter(lambda x: x.isalnum(), list(s.lower()))))
        return s == s[-1::-1]
