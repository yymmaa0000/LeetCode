# 246. Strobogrammatic Number
# Easy
# 140339FavoriteShare
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
# Example 1:
# Input:  "69"
# Output: true
# Example 2:
# Input:  "88"
# Output: true
# Example 3:
# Input:  "962"
# Output: false
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        ass = ["0","1","8"]
        fuck = ["0","1","6","8","9"]
        length = len(num)
        if length == 1: return num in ass
        if length%2: 
            mid = length//2
            if num[mid] not in ass: return False
            left = mid-1
            right = mid+1
        else:
            left = length//2-1
            right = length//2
        while left >= 0:
            #print (num[left],num[right])
            if num[left] not in fuck or num[right] not in fuck: return False
            if num[left] == "6":
                if num[right] != "9": return False
                else:
                    left -= 1
                    right += 1
                    continue
            if num[left] == "9":
                if num[right] != "6": return False
                else:
                    left -= 1
                    right += 1
                    continue
            if num[left] != num[right]: 
                return False
            left -= 1
            right += 1
        return True
