# 346. Moving Average from Data Stream
# Easy
# 33938FavoriteShare
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
# Example:
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.max_size = size
        

    def next(self, val: int) -> float:
        if len(self.queue) < self.max_size:
            self.queue.append(val)
            return sum(self.queue)/len(self.queue)
        self.queue.pop(0)
        self.queue.append(val)
        return sum(self.queue)/self.max_size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
