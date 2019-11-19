# 425. Word Squares
# Hard
# 38533FavoriteShare
# Given a set of words (without duplicates), find all word squares you can build from them.
# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
# b a l l
# a r e a
# l e a d
# l a d y
# Note:
# 1.  There are at least 1 and at most 1000 words.
# 2.  All words will have the exact same length.
# 3.  Word length is at least 1 and at most 5.
# 4.  Each word contains only lowercase English alphabet a-z.
# Example 1:
# Input:
# ["area","lead","wall","lady","ball"]

# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]

# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# Example 2:
# Input:
# ["abat","baba","atan","atal"]

# Output:
# [
#   [ "baba",
#     "abat",
#     "baba",
#     "atan"
#   ],
#   [ "baba",
#     "abat",
#     "baba",
#     "atal"
#   ]
# ]

# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        result = set()
        dic = {}
        n = len(words[0])
        for word in words:
            for i in range(n-1):
                prefix = word[:i+1]
                if prefix in dic: dic[prefix].append(word)
                else: dic[prefix]= [word]
                    
        def dfs(curr_list,n,dic,result):
            length = len(curr_list)
            if length == n:
                result.add(tuple(curr_list))
                return
            prefix = ""
            for x in curr_list:
                prefix += x[length]
            if prefix in dic:
                for poop in dic[prefix]:
                    dfs(curr_list+[poop],n,dic,result)
            return
        
        for word in words:
            dfs([word],n,dic,result)
        true_result = []
        for x in result: true_result.append(x)
        return true_result
