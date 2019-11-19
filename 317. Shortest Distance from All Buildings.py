# 317. Shortest Distance from All Buildings
# Hard
# 52029FavoriteShare
# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
# •   Each 0 marks an empty land which you can pass by freely.
# •   Each 1 marks a building which you cannot pass through.
# •   Each 2 marks an obstacle which you cannot pass through.
# Example:
# Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# Output: 7 
# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
#              the point (1,2) is an ideal empty land to build a house, as the total 
#              travel distance of 3+3+1=7 is minimal. So return 7.
# Note:
# There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def bfs(row,col,grid,visited,score,visit_count):
            queue = [[row+1,col],[row-1,col],[row,col+1],[row,col-1]]
            step = 1
            while len(queue) > 0:
                new_queue = []
                for row,col in queue:
                    #print(row,col)
                    if row < 0 or row >= len(grid): continue
                    if col < 0 or col >= len(grid[0]): continue
                    if grid[row][col] != 0: continue
                    if visited[row][col] == 1: continue
                    #print(row,col)
                    score[row][col] += step
                    visited[row][col] = 1
                    visit_count[row][col] += 1
                    new_queue.append([row+1,col])
                    new_queue.append([row-1,col])
                    new_queue.append([row,col+1])
                    new_queue.append([row,col-1])
                step += 1
                queue = new_queue
        house = []
        score = []
        for i in range(len(grid)):
            temp = [0] * len(grid[0])
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    house.append([i,j])
                    temp[j] = 2**31
                elif grid[i][j] == 2:
                    temp[j] = 2**31
                else:
                    temp[j] = 0
            score.append(temp)
        #print(house)
        #print(score)
        
        temp = [0]*len(grid[0])
        visit_count = [temp[:] for i in range(len(grid))]
        
        for row,col in house:
            temp = [0]*len(grid[0])
            visited = [temp[:] for i in range(len(grid))]
            bfs(row,col,grid,visited,score,visit_count)
            
        result = 2**31
        for i in range(len(score)):
            for j in range(len(score[0])):
                if score[i][j] > 0 and visit_count[i][j] == len(house): result = min(result,score[i][j])
        print(score)
        if result == 2**31: result = -1
        return result
                
        
