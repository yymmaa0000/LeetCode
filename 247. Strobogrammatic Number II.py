# 247. Strobogrammatic Number II
# Medium
# 26285FavoriteShare
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Find all strobogrammatic numbers that are of length = n.
# Example:
# Input:  n = 2
# Output: ["11","69","88","96"]
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 0: return []
        if n == 1: return ["0","1","8"]
        result = [""]
        end = [""]
        start = True
        for i in range(n//2):
            temp = []
            end_temp = []
            for i in range(len(result)):
                x = result[i]
                z = end[i]
                if start:
                    for y in ["1","6","8","9"]:
                        temp.append(x+y)
                        if y == "6":end_temp.append("9"+z)
                        elif y == "9":end_temp.append("6"+z)
                        else:end_temp.append(y+z)
                    start = False
                else:
                    for y in ["0","1","6","8","9"]:
                        temp.append(x+y)
                        if y == "6":end_temp.append("9"+z)
                        elif y == "9":end_temp.append("6"+z)
                        else:end_temp.append(y+z)
            result = temp
            end = end_temp
        """for i in range(len(end)):
            end[i] = reversed(end[i])"""
        print(result)
        print(end)
        ass = []
        if n%2:
            for i in range(len(result)):
                for y in ["0","1","8"]:
                    ass.append(result[i]+y+end[i])
        else:
            for i in range(len(result)): 
                ass.append(result[i]+end[i])
        return ass
