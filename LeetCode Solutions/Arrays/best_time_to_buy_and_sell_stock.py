# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Naive O(n^2) solution
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > max_profit:
        #             max_profit = prices[j] - prices[i]
        # return max_profit

        # Better solution, using two pointers (left pointer, right pointer)
        if len(prices) == 1:
            return 0
        left_ptr = 0
        right_ptr = 1
        max_profit = 0

        while right_ptr < len(prices):
            if prices[right_ptr] < prices[left_ptr]:
                left_ptr = right_ptr
                right_ptr += 1
            elif prices[right_ptr] - prices[left_ptr] > max_profit:
                max_profit = prices[right_ptr] - prices[left_ptr]
                right_ptr += 1
            else:
                right_ptr += 1
        return max_profit