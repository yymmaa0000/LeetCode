# 727. Minimum Window Subsequence
# Hard
# 35016FavoriteShare
# Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.
# If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.
# Example 1:
# Input: 
# S = "abcdebdde", T = "bde"
# Output: "bcde"
# Explanation: 
# "bcde" is the answer because it occurs before "bdde" which has the same length.
# "deb" is not a smaller window because the elements of T in the window must occur in order.
 
# Note:
# •   All the strings in the input will only contain lowercase letters.
# •   The length of S will be in the range [1, 20000].
# •   The length of T will be in the range [1, 100].
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        n = len(S)
        dp = [None]*n
        for key,val in enumerate(S):
            if val == T[0]: dp[key] = key
        for i in range(1,len(T)):
            dp_new = [None]*n
            start = None
            for key,val in enumerate(S):
                if start != None and val == T[i]:
                    dp_new[key] = start
                if dp[key] != None: start = dp[key]
            dp = dp_new
            
        result = (0,2**31)
        for key,val in enumerate(dp):
            if val != None:
                if key-val < result[1] - result[0]:
                    result = (val,key)
        if result == (0,2**31): return ""
        return S[result[0]:result[1]+1]
