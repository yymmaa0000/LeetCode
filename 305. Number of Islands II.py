# 305. Number of Islands II
# Hard
# 5909FavoriteShare
# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLandoperation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# Example:
# Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# Output: [1,1,2,3]
# Explanation:
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# Follow up:
# Can you do it in time complexity O(k log mn), where k is the length of the positions?
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        data = [-1 for i in range(m*n)]
        island = [[0]*n for i in range(m)]
        result = []
        overlap = set()
        
        def father(data,k):
            temp = k
            while data[temp] != temp:
                temp = data[temp]
            return temp
        
        cnt = 0
        for i,j in positions:
            #print(data)
            id = i*n+j
            
            if island[i][j] != 0: 
                result.append(result[-1])
                continue
            data[id] = id
            island[i][j] = 1
            cnt += 1
            neighboor = []
            overlap.clear()
            if i > 0 and island[i-1][j] == 1:
                #print(father(result,(i-1)*n+j))
                neighboor.append((i-1)*n+j)
            if i < m-1 and island[i+1][j] == 1:
                #print(father(result,(i+1)*n+j))
                neighboor.append((i+1)*n+j)
            if j > 0 and island[i][j-1] == 1:
                #print(father(result,i*n+j-1))
                neighboor.append(i*n+j-1)
            if j < n-1 and island[i][j+1] == 1:
                #print(father(result,i*n+j+1))
                neighboor.append(i*n+j+1)
            
            #print(neighboor)
            for x in neighboor:
                #print(x)
                overlap.add(father(data,x))
            cnt -= len(overlap)
            for x in overlap:
                data[x] = id
            #print(data)
            #print(overlap)
            '''count = set()
            for k in range(m*n):
                if data[k] == -1: continue
                count.add(father(result,k))
            result.append(len(count))'''
            
            result.append(cnt)
        return result
            
