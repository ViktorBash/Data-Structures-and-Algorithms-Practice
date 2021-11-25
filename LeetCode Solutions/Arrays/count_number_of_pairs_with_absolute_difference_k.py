# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Record how many times each number is in the array with the dictionary
        # There are 2 possible differences (abs value does this)
        # Check if these differences occur, and then add to the counter if they do
        # Divide the counter by 2 because we are counting each pair twice

        dictionary = {}
        counter = 0
        for i in range(len(nums)):
            if dictionary.has_key(nums[i]):
                dictionary[nums[i]] += 1
            else:
                dictionary[nums[i]] = 1

        for i in range(len(nums)):
            diff_1 = nums[i] - k
            diff_2 = nums[i] + k
            if diff_1 in dictionary:
                counter += dictionary[diff_1]
            if diff_2 in dictionary:
                counter += dictionary[diff_2]
        return counter / 2