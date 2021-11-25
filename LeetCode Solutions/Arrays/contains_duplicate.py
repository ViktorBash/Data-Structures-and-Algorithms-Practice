# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = {}
        for num in nums:
            if counter.has_key(num):
                return True
            else:
                counter[num] = 0
        return False
