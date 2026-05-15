class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # pattern to remember - plot a graph and that helps in coding the solution
        # loop through the array and update min value if curr value is smaller than the min
        # if not, compute the profit and see if that is greater than the current max profit
        ## 7 1 5 3 6 4
        min_price = float("inf") # positive inf, for neg inf -> float("-inf")
        max_profit = 0 
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > max_profit:
                max_profit = p-min_price
            
        return max_profit
