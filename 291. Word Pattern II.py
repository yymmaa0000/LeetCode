# 291. Word Pattern II
# Hard
# 29120FavoriteShare
# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.
# Example 1:
# Input: pattern = "abab", str = "redblueredblue"
# Output: true
# Example 2:
# Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
# Output: true
# Example 3:
# Input: pattern = "aabb", str = "xyzabcxzyabc"
# Output: false
# Notes:
# You may assume both pattern and str contains only lowercase letters.
class Solution:
    def wordPatternMatch(self, pattern: str, word: str) -> bool:
        dic = {}
        seen = set()
        
        def dfs(pi,wi,dic,seen):
            #print(dic,seen,pi,wi)
            if pi == len(pattern) and wi == len(word): return True
            elif pi >= len(pattern) or wi >= len(word): return False
            if pattern[pi] in dic:
                mapping = dic[pattern[pi]]
                if mapping != word[wi:wi+len(mapping)]: return False
                return dfs(pi+1,wi+len(mapping),dic,seen)
            else:
                for i in range(wi,len(word)-len(pattern)+pi+1):
                    mapping = word[wi:i+1]
                    if mapping in seen: continue
                    else:
                        dic[pattern[pi]] = mapping
                        seen.add(mapping)
                    if dfs(pi+1,i+1,dic,seen) == True: return True
                    else:
                        del dic[pattern[pi]] 
                        seen.remove(mapping)
            return False
        return dfs(0,0,dic,seen)
