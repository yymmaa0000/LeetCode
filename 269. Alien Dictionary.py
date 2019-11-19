# 269. Alien Dictionary
# Hard
# 998205FavoriteShare
# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
# Example 1:
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]

# Output: "wertf"
# Example 2:
# Input:
# [
#   "z",
#   "x"
# ]

# Output: "zx"
# Example 3:
# Input:
# [
#   "z",
#   "x",
#   "z"
# ] 

# Output: "" 

# Explanation: The order is invalid, so return "".
# Note:
# 1.  You may assume all letters are in lowercase.
# 2.  You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# 3.  If the order is invalid, return an empty string.
# 4.  There may be multiple valid order of letters, return any one of them is fine.
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        if n < 1: return ""
        
        child = {} # record chars that are behind the key char
        parent = {} # record how many chars are in front of the key char
        
        for word in words:
            for char in word:
                if char not in parent: parent[char] = 0
                    
        for i in range(n-1):
            a = words[i]
            b = words[i+1]
            for j in range(min(len(a),len(b))):
                if a[j] != b[j]:
                    if a[j] not in child: child[a[j]] = [b[j]]
                    else: child[a[j]].append(b[j])
                    parent[b[j]] += 1
                    break
        #print(child,parent)
        queue = []
        for key,val in parent.items():
            if val == 0: queue.append(key)
        
        result = []
        while queue:
            x = queue.pop(0)
            result.append(x)
            if x not in child: continue
            for baby in child[x]:
                parent[baby] -= 1
                if parent[baby] == 0: queue.append(baby)
        
        if len(result) != len(parent): return ""
        return "".join(result)
