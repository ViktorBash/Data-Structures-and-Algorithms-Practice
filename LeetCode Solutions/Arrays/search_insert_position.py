# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # O(n) solution
        # target_index = None
        # for i in range(len(nums)):
        #     if target <= nums[i]:
        #         return i
        # return len(nums)

        # O(logn) solution using binary search

        if len(nums) == 1 and target <= nums[0]:
            return 0
        elif len(nums) == 1:
            return 1

        low = 0
        high = len(nums) - 1
        while low <= high:
            # print(low)
            # print(high)
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return low