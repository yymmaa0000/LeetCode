# 159. Longest Substring with At Most Two Distinct Characters
# Hard
# 60312FavoriteShare
# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.
# Example 1:
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# Example 2:
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        result = 0
        if len(s)<2:return len(s)
        dic = {}
        start = 0
        for i in range(len(s)):
            if len(dic) < 2:
                if s[i] in dic: dic[s[i]] += 1
                else: dic[s[i]] = 1
            elif s[i] in dic: dic[s[i]] += 1
            else:
                for j in range(start,i):
                    dic[s[j]] -= 1
                    if dic[s[j]] == 0: 
                        del dic[s[j]]
                        start = j+1
                        break
                dic[s[i]] = 1
            result = max(result,sum(dic.values()))
        return result
