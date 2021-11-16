# https://leetcode.com/problems/two-sum/submissions/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # O(n^2) naive solution
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j != i and nums[i] + nums[j] == target:
        #             return [i, j]

        # Use a hashmap, O(n) solution
        difference = {}
        for i in range(len(nums)):
            if difference.has_key(target - nums[i]):
                return [difference[target - nums[i]], i]
            else:
                difference[nums[i]] = i
