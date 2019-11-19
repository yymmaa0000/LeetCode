# 489. Robot Room Cleaner
# Hard
# 60333FavoriteShare
# Given a robot cleaner in a room modeled as a grid.
# Each cell in the grid can be empty or blocked.
# The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.
# When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.
# Design an algorithm to clean the entire room using only the 4 given APIs shown below.
# interface Robot {
#   // returns true if next cell is open and robot moves into the cell.
#   // returns false if next cell is obstacle and robot stays on the current cell.
#   boolean move();

#   // Robot will stay on the same cell after calling turnLeft/turnRight.
#   // Each turn will be 90 degrees.
#   void turnLeft();
#   void turnRight();

#   // Clean the current cell.
#   void clean();
# }
# Example:
# Input:
# room = [
#   [1,1,1,1,1,0,1,1],
#   [1,1,1,1,1,0,1,1],
#   [1,0,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0,0],
#   [1,1,1,1,1,1,1,1]
# ],
# row = 1,
# col = 3

# Explanation:
# All grids in the room are marked by either 0 or 1.
# 0 means the cell is blocked, while 1 means the cell is accessible.
# The robot initially starts at the position of row=1, col=3.
# From the top left corner, its position is one row below and three columns right.
# Notes:
# 1.  The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the mentioned 4 APIs, without knowing the room layout and the initial robot's position.
# 2.  The robot's initial position will always be in an accessible cell.
# 3.  The initial direction of the robot will be facing up.
# 4.  All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
# 5.  Assume all four edges of the grid are all surrounded by wall.
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def clean_your_ass(robot,x,y,DP):
            robot.clean()
            DP[y][x] = 4
            #print(DP)
            #print(x,y)
            
            if DP[y-1][x] == -1:
                if robot.move() == False: DP[y-1][x] = 0
                else: 
                    clean_your_ass(robot,x,y-1,DP)
                    robot.turnRight();
                    robot.turnRight();
                    robot.move();
                    robot.turnRight();
                    robot.turnRight();
            if DP[y+1][x] == -1:
                robot.turnRight();
                robot.turnRight();
                if robot.move() == False: 
                    DP[y+1][x] = 0
                    robot.turnRight();
                    robot.turnRight();
                else: 
                    robot.turnRight();
                    robot.turnRight();
                    clean_your_ass(robot,x,y+1,DP)
                    robot.move();
            if DP[y][x-1] == -1:
                robot.turnLeft();
                if robot.move() == False: 
                    DP[y+1][x] = 0
                    robot.turnRight();
                else: 
                    robot.turnRight();
                    clean_your_ass(robot,x-1,y,DP)
                    robot.turnRight();
                    robot.move();
                    robot.turnLeft();
            if DP[y][x+1] == -1:
                robot.turnRight();
                if robot.move() == False: 
                    DP[y+1][x] = 0
                    robot.turnLeft();
                else: 
                    robot.turnLeft();
                    clean_your_ass(robot,x+1,y,DP)
                    robot.turnLeft();
                    robot.move();
                    robot.turnRight();
                
                    
        DP = []
        for i in range(1000):
            ass = [-1]*1000
            DP.append(ass)
        startx = 500
        starty = 500
        clean_your_ass(robot,startx,starty,DP)
        return
