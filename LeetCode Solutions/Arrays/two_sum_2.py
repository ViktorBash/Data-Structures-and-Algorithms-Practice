# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in dictionary:
                return [dictionary[difference] + 1, i + 1]
            dictionary[numbers[i]] = i
