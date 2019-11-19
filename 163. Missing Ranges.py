# 163. Missing Ranges
# Medium
# 2291340FavoriteShare
# Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
# Example:
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if nums == []: 
            if lower == upper: return[str(lower)]
            return[str(lower)+"->"+str(upper)]
        prev = lower-1
        result = []
        for x in nums:
            print(prev,x)
            if x == prev+2:
                result.append(str(prev+1))
            elif x > prev+2:
                result.append(str(prev+1)+"->"+str(x-1))
            prev = x
        if x == upper-1: result.append(str(upper))
        elif x < upper -1: result.append(str(x+1)+"->"+str(upper))
        return result
