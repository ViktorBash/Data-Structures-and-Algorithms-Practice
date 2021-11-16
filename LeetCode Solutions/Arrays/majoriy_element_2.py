# https://leetcode.com/problems/majority-element-ii/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # First thought: loop through the list, record the occurence of each number in a hash map
        # Loop through again, fill a return array with everything that has an occurence greater than n / 3
        dictionary = {}
        for num in nums:
            if dictionary.has_key(num):
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        threshold = len(nums) / 3
        result = []
        for key, value in dictionary.items():
            if value > threshold:
                result.append(key)
        return result
