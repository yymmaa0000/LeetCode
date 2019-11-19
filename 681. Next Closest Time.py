# 681. Next Closest Time
# Medium
# 369588FavoriteShare
# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
# Example 1:
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
class Solution:
    def nextClosestTime(self, time: str) -> str:
        ass = time.split(":")
        hour = ass[0]
        mins = ass[1]
        characters = list(hour)+list(mins)
        integers = []
        for x in characters: integers.append(int(x))
        #print(integers)
        
        digit_min = min(integers)
        for i in range(integers[3]+1,10):
            if i in integers:
                return hour+":"+mins[0]+str(i)
        for i in range(integers[2]+1,6): 
            if i in integers:
                return hour+":"+str(i)+str(digit_min)
        if integers[0] < 2:
            for i in range(integers[1]+1,10):
                if i in integers:
                    return hour[0]+str(i)+":"+str(digit_min)+str(digit_min)
            for i in range(integers[0]+1,3):
                if i in integers: return str(i)+str(digit_min)+":"+str(digit_min)+str(digit_min)
        else:
            for i in range(integers[1]+1,4): 
                if i in integers:
                    return "2"+str(i)+":"+str(digit_min)+str(digit_min)
        return str(digit_min)+str(digit_min)+":"+str(digit_min)+str(digit_min)
