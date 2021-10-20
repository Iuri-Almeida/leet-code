class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        l = []
        s = ''
        for i in range(len(nums)):
            if i == 0:
                s += str(nums[i])
            else:
                if nums[i] - 1 == nums[i - 1]:
                    s = str(s.split("->")[0]) + '->' + str(nums[i])
                else:
                    l.append(s)
                    s = str(nums[i])
        if s: l.append(s)
        return l