# 265. Paint House II
# Hard
# 37312FavoriteShare
# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.
# Note:
# All costs are positive integers.
# Example:
# Input: [[1,5,3],[2,9,4]]
# Output: 5
# Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
#              Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
# Follow up:
# Could you solve it in O(nk) runtime?
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if costs == []: return 0
        color = len(costs[0])
        house = len(costs)
        if house == 1 and color == 1: return costs[0][0]
        dp = [[2**31]*color for i in range(house+1)]
        for i in range(color):
            dp[-1][i] = 0
        #print(dp)
        for i in reversed(range(house)):
            for j in range(color):
                for k in range(color):
                    if k == j: continue
                    dp[i][j] = min(dp[i][j],costs[i][j]+dp[i+1][k])
        #print(dp)
        return min(dp[0])
