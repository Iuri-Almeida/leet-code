class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return 0 if haystack == needle == '' else (haystack.index(needle) if needle in haystack else -1)