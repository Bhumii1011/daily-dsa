class Solution:
    def knapsack(self, W, val, wt):
        n = len(wt)
        dp = [0]*(W+1)
        
        for i in range(n):

            weight = wt[i]
            value = val[i]
            
            for capacity in range(W,weight-1,-1):
                
                dp[capacity] = max(dp[capacity], value+dp[capacity-weight])
            
        return dp[W]