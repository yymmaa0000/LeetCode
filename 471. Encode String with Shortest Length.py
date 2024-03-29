# 471. Encode String with Shortest Length
# Hard
# 25516FavoriteShare
# Given a non-empty string, encode the string such that its encoded length is the shortest.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
# Note:
# 1.  k will be a positive integer and encoded string will not be empty or have extra space.
# 2.  You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
# 3.  If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.
 
# Example 1:
# Input: "aaa"
# Output: "aaa"
# Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
 
# Example 2:
# Input: "aaaaa"
# Output: "5[a]"
# Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
 
# Example 3:
# Input: "aaaaaaaaaa"
# Output: "10[a]"
# Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
 
# Example 4:
# Input: "aabcaabcd"
# Output: "2[aabc]d"
# Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
 
# Example 5:
# Input: "abbbabbbcabbbabbbc"
# Output: "2[2[abbb]c]"
# Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".
class Solution:
    def encode(self, s: str) -> str:
        data = {}
        def dfs(s,data):
            if len(s)<5: return s
            if s in data: return data[s]
            result = s
            for i in range(1,len(s)//2+1):
                temp = s[:i]
                if len(s)%len(temp) == 0 and s == temp*(len(s)//len(temp)):
                    temp_result = str(len(s)//len(temp))+"["+dfs(temp,data)+"]"
                    if len(temp_result)<len(result):result = temp_result
            for i in range(len(s)-1):
                temp_result = dfs(s[0:i+1],data)+dfs(s[i+1:],data)
                if len(temp_result)<len(result):result = temp_result
            data[s] = result
            return result
        return dfs(s,data)
