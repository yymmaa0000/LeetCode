# 353. Design Snake Game
# Medium
# 25494FavoriteShare
# Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.
# The snake is initially positioned at the top left corner (0,0) with length = 1 unit.
# You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.
# Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.
# When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.
# Example:
# Given width = 3, height = 2, and food = [[1,2],[0,1]].

# Snake snake = new Snake(width, height, food);

# Initially the snake appears at position (0,0) and the food at (1,2).

# |S| | |
# | | |F|

# snake.move("R"); -> Returns 0

# | |S| |
# | | |F|

# snake.move("D"); -> Returns 0

# | | | |
# | |S|F|

# snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

# | |F| |
# | |S|S|

# snake.move("U"); -> Returns 1

# | |F|S|
# | | |S|

# snake.move("L"); -> Returns 2 (Snake eats the second food)

# | |S|S|
# | | |S|

# snake.move("U"); -> Returns -1 (Game over because snake collides with border)
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = food
        self.body = []
        self.head = [0,0]
        self.score = 0
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        new_head = self.head.copy()
        if direction == "U": new_head[0] -= 1
        elif direction == "D": new_head[0] += 1
        elif direction == "L": new_head[1] -= 1
        elif direction == "R": new_head[1] += 1
        else: return
        
        if new_head[0] < 0 or new_head[0] >= self.height or new_head[1] < 0 or new_head[1] >= self.width: return -1
        
        
        print(new_head)
        if len(self.food) >0 and new_head == self.food[0]:
            self.food.pop(0)
            self.body.append(self.head)
            self.head = new_head
            self.score += 1
            return self.score
        else:
            self.body.append(self.head)
            self.body.pop(0)
            self.head = new_head
            if new_head in self.body: return -1
            return self.score
            
            
        
            
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
