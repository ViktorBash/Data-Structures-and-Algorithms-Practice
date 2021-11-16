# https://leetcode.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # O(n) solution, not O(1) space
        # counter = {}
        # for num in nums:
        #     if counter.has_key(num):
        #         counter[num] += 1
        #     else:
        #         counter[num] = 1
        # max_element = nums[0]
        # for key, value in counter.items():
        #     if value > counter[max_element]:
        #         max_element = key
        # return max_element

        # Intuition: majority element is in more than half of list, if we add 1 when we see it and subtract 1 when we
        # don't, we will easily see what the majority element is
        # O(n) solution using Boyer-Moore Voting Algorithm, O(1) space
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num != candidate:
                count -= 1
            if num == candidate:
                count += 1
        return candidate