# 527. Word Abbreviation
# Hard
# 16199FavoriteShare
# Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.
# 1.  Begin with the first character and then the number of characters abbreviated, which followed by the last character.
# 2.  If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
# 3.  If the abbreviation doesn't make the word shorter, then keep it as original.
# Example:
# Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
# Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
# Note:
# 1.  Both n and the length of each word will not exceed 400.
# 2.  The length of each word is greater than 1.
# 3.  The words consist of lowercase English letters only.
# 4.  The return answers should be in the same order as the original array.
class Trie:
    def __init__ (self,val):
        self.val = val
        self.next = {}
        
class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        forest = {}
        
        for word in dict:
            if len(word)<4: continue
            encode = word[0]+str(len(word))+word[-1]
            if encode not in forest: forest[encode] = Trie(0)
            current = forest[encode]
            for x in word:
                if x not in current.next:
                    current.next[x] = Trie(1)
                else:
                    current.next[x].val += 1
                current = current.next[x]
        
        result = []
        for word in dict:
            if len(word)<4: 
                result.append(word)
                continue
            encode = word[0]+str(len(word))+word[-1]
            current = forest[encode]
            for i,x in enumerate(word):
                if i >= len(word)-3: 
                    result.append(word)
                    break
                current = current.next[x]
                if current.val == 1:
                    temp = word[:i+1]+str(len(word)-2-i)+word[-1]
                    result.append(temp)
                    break
        return result
