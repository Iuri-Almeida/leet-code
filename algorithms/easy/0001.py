class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for n in range(len(nums)):
            for i in range(n + 1, len(nums)):
                if (nums[n] + nums[i]) == target:
                    return [n, i]
