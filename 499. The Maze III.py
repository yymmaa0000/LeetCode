# 499. The Maze III
# Hard
# 12236FavoriteShare
# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up(u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.
# Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving the shortest distance. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the hole (included). Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.
 
# Example 1:
# Input 1: a maze represented by a 2D array

# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0

# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (0, 1)

# Output: "lul"

# Explanation: There are two shortest ways for the ball to drop into the hole.
# The first way is left -> up -> left, represented by "lul".
# The second way is up -> left, represented by 'ul'.
# Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".
 
# Example 2:
# Input 1: a maze represented by a 2D array

# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0

# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (3, 0)

# Output: "impossible"

# Explanation: The ball cannot reach the hole.
 
 
# Note:
# 1.  There is only one ball and one hole in the maze.
# 2.  Both the ball and hole exist on an empty space, and they will not be at the same position initially.
# 3.  The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
# 4.  The maze contains at least 2 empty spaces, and the width and the height of the maze won't exceed 30.
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        result = ["Z",2**31]
        
        def dfs(maze,hole,i,j,distance,path,visited,result):
            #print(result)
            if (i,j) in visited and visited[(i,j)] < distance: return
            #print(i,j)
            visited[(i,j)] = distance
            
            # go up
            traveled = 0
            ii = i
            while ii > 0 and maze[ii-1][j] == 0:
                ii -= 1
                traveled += 1
                if [ii,j] == hole:
                    if traveled + distance <= result[1]:
                        path.append("u")
                        temp_result = "".join(path)
                        if traveled + distance < result[1] or temp_result  < result[0]:
                            result[0] = temp_result
                            result[1] = traveled + distance
                        path.pop()
                        return
                    return
            if ii != i:
                path.append("u")
                dfs(maze,hole,ii,j,distance+traveled,path,visited,result)
                path.pop()
            
            # go down
            traveled = 0
            ii = i
            while ii < len(maze)-1 and maze[ii+1][j] == 0:
                ii += 1
                traveled += 1
                if [ii,j] == hole:
                    if traveled + distance <= result[1]:
                        path.append("d")
                        temp_result = "".join(path)
                        if traveled + distance < result[1] or temp_result < result[0]:
                            result[0] = temp_result
                            result[1] = traveled + distance
                        path.pop()
                        return
                    return
            if ii != i:
                path.append("d")
                dfs(maze,hole,ii,j,distance+traveled,path,visited,result)
                path.pop()
            
            # go left
            traveled = 0
            jj = j
            while jj > 0 and maze[i][jj-1] == 0:
                jj -=1
                traveled += 1
                if [i,jj] == hole:
                    if traveled + distance <= result[1]:
                        #print(traveled + distance)
                        path.append("l")
                        temp_result = "".join(path)
                        if traveled + distance < result[1] or temp_result < result[0]:
                            result[0] = temp_result
                            result[1] = traveled + distance
                        path.pop()
                        return
                    return
            if jj != j:
                path.append("l")
                dfs(maze,hole,i,jj,distance+traveled,path,visited,result)
                path.pop()
            
            # go right
            traveled = 0
            jj = j
            while jj < len(maze[0])-1 and maze[i][jj+1] == 0:
                jj +=1
                traveled += 1
                if [i,jj] == hole:
                    if traveled + distance <= result[1]:
                        path.append("r")
                        temp_result = "".join(path)
                        if traveled + distance < result[1] or temp_result < result[0]:
                            result[0] = temp_result
                            result[1] = traveled + distance
                        path.pop()
                        return
                    return
            if jj != j:
                path.append("r")
                dfs(maze,hole,i,jj,distance+traveled,path,visited,result)
                path.pop()
                
            
                
        visited = {}
        dfs(maze,hole,ball[0],ball[1],0,[],visited,result)
        if result[0] == "Z": return "impossible"
        return result[0]
