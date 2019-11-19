# 644. Maximum Average Subarray II
# Hard
# 29932FavoriteShare
# Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.
# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation:
# when length is 5, maximum average value is 10.8,
# when length is 6, maximum average value is 9.16667.
# Thus return 12.75.
# Note:
# 1.  1 <= k <= n <= 10,000.
# 2.  Elements of the given array will be in range [-10,000, 10,000].
# 3.  The answer with the calculation error less than 10-5 will be accepted.
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def is_good(nums,avg,k):
            right = 0
            for i in range(k):
                right += nums[i] - avg
            if right >= 0: return True
            best_left = 0
            left = 0
            for i in range(k,len(nums)):
                right += nums[i] - avg
                left += nums[i-k] - avg
                best_left = min(best_left,left)
                if right - best_left >= 0: return True
            return False
        l = min(nums)
        r = max(nums)
        while r - l > 10**-5:
            mid = (r+l)/2
            if is_good(nums,mid,k): l = mid
            else: r = mid
        return l
