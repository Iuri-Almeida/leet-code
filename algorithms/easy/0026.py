class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in nums:
            k = nums[nums.index(n):(nums.index(n) + nums.count(n)) - 1]
            for c in k:
                nums.remove(c)
        return len(nums)
