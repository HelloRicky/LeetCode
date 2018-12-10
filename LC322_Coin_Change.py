"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # MAX = float('inf')
        # dp = [0] + [MAX] * amount
        # for i in range(1, amount + 1):
        #   dp[i] = min([dp[i-c] if i-c >= 0 else MAX for c in coins]) + 1
        # return dp[amount] if dp[amount] < MAX else -1
        
        ## top answer
        def helper(idx, a, nCoins):
            global bestNCoins
            # lower bound on number of coins, achieved using the biggest coin
            lowerBound = nCoins + (a + sortedCoins[idx] - 1) / sortedCoins[idx]

            if lowerBound >= bestNCoins:
                return

            # if amount matches the biggest coin, that is the solution
            if a == sortedCoins[idx] and nCoins + 1 < bestNCoins:
                bestNCoins = nCoins + 1
                return

            # try use the biggest coin
            if a > sortedCoins[idx]:
                helper(idx, a - sortedCoins[idx], nCoins + 1)

            # else try not to use the biggest coin
            if idx < len(sortedCoins) - 1:
                helper(idx + 1, a, nCoins)
                  
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0

        # try biggest coins first
        sortedCoins = sorted(coins, reverse=True)

        # upper bound on number of coins (+1 to represent the impossible case)
        upperBound = (amount + sortedCoins[-1] - 1) / sortedCoins[-1] + 1
        print upperBound

        global bestNCoins
        bestNCoins = upperBound

        helper(0, amount, 0)

        if bestNCoins == upperBound:
            return -1
        else:
            return bestNCoins