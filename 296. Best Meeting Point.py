# 296. Best Meeting Point
# Hard
# 31322FavoriteShare
# A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
# Example:
# Input: 

# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0

# Output: 6 

# Explanation: Given three people living at (0,0), (0,4), and (2,2):
#              The point (0,2) is an ideal meeting point, as the total travel distance 
#              of 2+2+2=6 is minimal. So return 6.
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        def med(li):
            if len(li)%2: return li[len(li)//2]
            else: return
        hori= []
        ver = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    hori.append(j)
                    ver.append(i)
        #print(hori)
        #print(ver)
        hori.sort()
        ver.sort()
        mid_x = hori[len(hori)//2]
        mid_y = ver[len(ver)//2]
        result = 0
        for x in hori:
            result += abs(x-mid_x)
        for x in ver:
            result += abs(x-mid_y)
        return result
        
