class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        if(n == 2) return cost[0] > cost[1] ? cost[1] : cost[0];

        vector<int> dp(n,0);
        dp[0] = cost[0]; dp[1] = cost[1];
        for(int i = 2; i < n; i++){
            dp[i] = min(dp[i - 1], dp[i -2]) + cost[i];
        }

        return min(dp[n-2] , dp[n-1]);
    }
};