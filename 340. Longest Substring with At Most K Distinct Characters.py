# 340. Longest Substring with At Most K Distinct Characters
# Hard
# 63320FavoriteShare
# Given a string, find the length of the longest substring T that contains at most k distinct characters.
# Example 1:
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        if len(s) == 0: return 0
        dic = {}
        result_l = 0
        result_r = 0
        result_length = 0
        l = 0
        r = 0
        for i in range(len(s)):
            if s[i] in dic: 
                dic[s[i]] += 1
            else:
                if len(dic) < k:
                    dic[s[i]] = 1
                else:
                    while len(dic) >= k:
                        dic[s[l]] -= 1
                        if dic[s[l]] == 0:
                            del dic[s[l]]
                        l += 1
                    dic[s[i]] = 1
            r = i
            if (r-l+1) > result_length:
                result_length = r-l+1
                result_l = l
                result_r = r
        #return s[result_l:result_r+1]
        return result_length
