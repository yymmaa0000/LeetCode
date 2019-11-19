// 1066. Campus Bikes II
// Medium
// 1365FavoriteShare
// On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.
// We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.
// The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
// Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.
 
// Example 1:
 
// Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
// Output: 6
// Explanation: 
// We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.
// Example 2:
 
// Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
// Output: 4
// Explanation: 
// We first assign bike 0 to worker 0, then assign bike 1 to worker 1 or worker 2, bike 2 to worker 2 or worker 1. Both assignments lead to sum of the Manhattan distances as 4.
 
// Note:
// 1.  0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000
// 2.  All worker and bike locations are distinct.
// 3.  1 <= workers.length <= bikes.length <= 10
class Solution {
public:
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        int n = bikes.size();
        vector<vector<int>> dp(workers.size()+1,vector<int>(1<<n,INT_MAX));
        dp[0][0] = 0;
        
        for (int w = 0; w< workers.size();w++){
            for (int bike_mask = 0; bike_mask < 1<<n; bike_mask ++){
                for (int b = 0; b < bikes.size();b++){
                    if (bike_mask & (1<<b)) continue;
                    if (dp[w][bike_mask] == INT_MAX) continue;
                    int new_bike_mask = bike_mask | (1<<b);
                    dp[w+1][new_bike_mask] = min(dp[w+1][new_bike_mask], dp[w][bike_mask] + abs(workers[w][0] - bikes[b][0])+abs(workers[w][1] - bikes[b][1]));
                }
            }
        }
        
        // for (int i = 0; i < workers.size()+1;i++){
        //     for (int j = 0; j < 1<<n;j++){
        //         cout<<dp[i][j]<<",";
        //     }
        //     cout<<endl;
        // }
    
        return *min_element(dp[workers.size()].begin(), dp[workers.size()].end());
    }
};
