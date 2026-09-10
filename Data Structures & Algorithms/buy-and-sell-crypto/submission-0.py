class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        best_profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                if best_profit > profit:
                    right +=1
                else:
                    best_profit = profit
                    right +=1
            else:
                left = right
                right += 1
        return best_profit