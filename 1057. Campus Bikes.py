# 1057. Campus Bikes
# Medium
# 12822FavoriteShare
# On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.
# Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.
# The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
# Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.
 
# Example 1:
 
# Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
# Output: [1,0]
# Explanation: 
# Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].
# Example 2:
 
# Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
# Output: [0,2,1]
# Explanation: 
# Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So the output is [0,2,1].
 
# Note:
# 1.  0 <= workers[i][j], bikes[i][j] < 1000
# 2.  All worker and bike locations are distinct.
# 3.  1 <= workers.length <= bikes.length <= 1000
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def dis(x,y):
            return abs(x[0]-y[0])+abs(x[1]-y[1])
        
        '''result = [-1] * len(workers)
        used = [0] * len(bikes)
        for w in range(len(workers)):
            minimum = 2**31
            min_index = -1
            for b in range(len(bikes)):
                if used[b]: continue
                ass = dis(workers[w],bikes[b])
                if ass < minimum:
                    minimum = ass
                    min_index = b
            result[w] = min_index
            used[min_index] = 1
        return result'''
        data = []
        for w in range(len(workers)):
            for b in range(len(bikes)):
                data.append([dis(workers[w],bikes[b]),w,b])
        data.sort()
        used_worker = [0]*len(workers)
        used_bike = [0]*len(bikes)
        result = [-1]*len(workers)
        for x,y,z in data:
            if used_worker[y] == 0 and used_bike[z] == 0:
                result[y]=z
                used_worker[y] = 1
                used_bike[z] = 1
        return result
