# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dictionary = {}
        if k == 0:
            for num in nums:
                if num in dictionary:
                    dictionary[num] += 1
                else:
                    dictionary[num] = 1
            counter = 0
            for value, key in dictionary.items():
                if key > 1:
                    counter += 1
            return counter

        counter = 0
        nums = list(set(nums))
        dictionary = {}
        for num in nums:
            dictionary[num] = 0
        for num in nums:
            diff_1 = num - k
            diff_2 = num + k
            if diff_1 in dictionary:
                counter += 1
            if diff_2 in dictionary:
                counter += 1
        return counter / 2