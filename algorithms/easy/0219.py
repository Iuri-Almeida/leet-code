class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) != len(set(nums)):
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] == nums[j] and abs(i - j) <= k:
                        return True
        return False